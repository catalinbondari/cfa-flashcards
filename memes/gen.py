#!/usr/bin/env python3
"""Generate meme images via codex exec. Resumable via memes/manifest.json.
usage: gen.py [--workers N] [--ids 12,13,...] [--limit K]"""
from PIL import Image
import json, os, subprocess, sys, time, argparse, threading
from concurrent.futures import ThreadPoolExecutor, as_completed

MEMES = '/Users/catalin_main/Code/cfa-flashcards/memes'
RAW = os.path.expanduser('~/.cache/cfa-memes-raw')
STYLE = ("Background: solid flat very dark navy (#131519) filling the entire canvas edge to edge, "
         "never white or light. Bold flat cartoon illustration, thick dark outlines, limited bright palette, "
         "one clear central subject drawn large, filling most of the square frame, close-up framing, "
         "a single continuous scene (no comic panels, frames or borders), exaggerated and funny expressions. "
         "Absolutely no text, letters, numbers, words, labels or signs anywhere in the image")
LIMIT_MARKERS = ('usage limit', 'rate limit', "you've hit", 'quota', 'too many requests')

ap = argparse.ArgumentParser()
ap.add_argument('--workers', type=int, default=3)
ap.add_argument('--ids', default='')
ap.add_argument('--limit', type=int, default=0)
ap.add_argument('--retry-failed', action='store_true')
a = ap.parse_args()

os.makedirs(RAW, exist_ok=True)
scenes = json.load(open(f'{MEMES}/scenes.json'))
mpath = f'{MEMES}/manifest.json'
man = json.load(open(mpath)) if os.path.exists(mpath) else {'done': [], 'failed': {}, 'style': STYLE}
man['style'] = STYLE
done = set(man['done'])
ids = [int(x) for x in a.ids.split(',')] if a.ids else sorted(int(k) for k in scenes)
INBOX = os.environ.get('MEME_INBOX', '')
todo = [i for i in ids if i not in done and not (INBOX and os.path.exists(f'{INBOX}/{i:03d}.jpg')) and (a.retry_failed or str(i) not in man['failed'])]
START_AT = int(os.environ.get('MEME_START', '250'))
todo = [i for i in todo if i >= START_AT] + [i for i in todo if i < START_AT]
if a.limit: todo = todo[:a.limit]
lock = threading.Lock()
stop = threading.Event()

def save():
    man['done'] = sorted(set(man['done']))
    tmp = mpath + '.tmp'
    json.dump(man, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, mpath)

def border_lum(path):
    im = Image.open(path).convert('L'); w, h = im.size; px = im.load()
    pts = [px[x, y] for x in range(0, w, 8) for y in (2, h - 3)] + [px[x, y] for y in range(0, h, 8) for x in (2, w - 3)]
    return sum(pts) / len(pts)

def gen(i):
    if stop.is_set(): return i, 'skipped', None
    name = f'{i:03d}'
    png, jpg = f'{RAW}/{name}.png', f'{MEMES}/{name}.jpg'
    prompt = (f"Use your image generation tool to create ONE square image and save it as {name}.png "
              f"in the current directory. Style: {STYLE}. Scene: {scenes[str(i)]['prompt']} "
              f"Pass the style and scene to the image tool faithfully, keeping the dark navy background. "
              f"Print only the file path.")
    reason = 'no output'
    for attempt in range(3):
        if os.path.exists(png): os.remove(png)
        try:
            r = subprocess.run(['codex', 'exec', '--skip-git-repo-check', '-C', RAW,
                                '--sandbox', 'workspace-write', prompt],
                               capture_output=True, text=True, timeout=420, stdin=subprocess.DEVNULL)
            out = (r.stdout + r.stderr)
        except subprocess.TimeoutExpired:
            out = 'timeout'
        if os.path.exists(png) and os.path.getsize(png) > 10000:
            subprocess.run(['sips', '-Z', '512', '-s', 'format', 'jpeg', '-s', 'formatOptions', '70',
                            png, '--out', jpg], capture_output=True)
            if not os.path.exists(jpg): return i, 'fail', 'sips failed'
            if border_lum(jpg) > 70 and attempt < 2:
                reason = 'light background'; continue
            return i, 'ok', ('light background kept' if border_lum(jpg) > 70 else None)
        open(f'{RAW}/{name}.err.log', 'w').write(out)
        errl = '\n'.join(l for l in out.lower().splitlines() if 'error' in l or 'usage limit' in l or "you've hit" in l)
        if any(m in errl for m in LIMIT_MARKERS):
            return i, 'limit', out.strip().splitlines()[-1][:200] if out.strip() else 'limit'
        reason = out.strip().splitlines()[-1][:200] if out.strip() else 'no output'
    return i, 'fail', reason

t0 = time.time(); n = 0
print(f'todo {len(todo)}, workers {a.workers}', flush=True)
with ThreadPoolExecutor(a.workers) as ex:
    futs = [ex.submit(gen, i) for i in todo]
    for f in as_completed(futs):
        i, st, why = f.result()
        with lock:
            if st == 'ok':
                man['done'].append(i); man['failed'].pop(str(i), None); n += 1
                if why: man.setdefault('light_bg', []).append(i)
            elif st == 'limit':
                man['failed'][str(i)] = f'usage limit: {why}'; stop.set()
            elif st == 'fail':
                man['failed'][str(i)] = why
            save()
            if st != 'skipped':
                print(f'{i:03d} {st} {why or ""} | done {len(set(man["done"]))}/502 '
                      f'{(time.time()-t0)/60:.1f}min', flush=True)
            if n and n % 25 == 0 and st == 'ok':
                print(f'PROGRESS {len(set(man["done"]))}/502', flush=True)
if stop.is_set(): print('STOPPED: usage limit hit', flush=True)
print('END', flush=True)

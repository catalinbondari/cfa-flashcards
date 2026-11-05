import json, os
R=os.path.expanduser('~/Code/cfa-flashcards')
cards=json.load(open('cards.json'))
sc=json.load(open(R+'/memes/scenes.json'))
for n,c in enumerate(cards):
    s=sc.get(str(n))
    if s and s.get('scene'): c['ms']=s['scene']; c['me']=s.get('emoji','')
data=json.dumps(cards,ensure_ascii=False).replace('</','<\\/')
open('deck.html','w').write(open('tpl.html').read().replace('__CARDS__',data))

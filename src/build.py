import json, re

RANGES = {
 'batch1.txt': [(1,13,'quant'),(14,51,'quant'),(52,74,'econ'),(75,105,'alts'),(106,120,'alts'),(121,136,'fi')],
 'batch2.txt': [(1,47,'fi'),(48,59,'fi'),(60,73,'deriv'),(74,87,'corp'),(88,123,'fsa')],
 'batch3.txt': [(1,57,'fsa'),(58,103,'ethics'),(104,128,'quant')],
 'batch4.txt': [(1,52,'pm'),(53,112,'equity')],
}

OVERRIDE = [
 (r'^(Constant Dividend Growth|Holding Period Return)', 'equity'),
 (r'^(Forward Rate|FR Currency|Hedge Ratio|Forward|F0)', 'deriv'),
 (r'^(Concentration Ratio|HHI|Cabotage|Exogenous|Perfect comp)', 'econ'),
 (r'^(Warrant|Futures contract|Forward contract|Commodity swap|Embedded derivative|OTC vs ETP)', 'deriv'),
 (r'^(Pari passu|Coupon|Covenant|Affirmative|Negative covenant|Floating Rate note|Matrix pricing)', 'fi'),
 (r'^(Fiduciary|Compliance approach|Ethical|Suitability|Ethical framework)', 'ethics'),
 (r'^(Fin leverage|Standards of Professional)', 'ethics'),
 (r'^(Real exchange Rate|FORWARD Rate \(currency\)|Fiscal policy|Monetary policy|CB policy|Financial tool geopolitics)', 'econ'),
 (r'^(Pearson|Spearman|Systematic sampling|Geometric Return|F-test|Chi-square|Continuous compounded|Machine learning)', 'quant'),
 (r'^(Sarbanes|Going concern|Changes in accounting|IFRS and US GAAP|Organic growth|Conv bond|Return on equity|IFRS other comp|Impairment loss|Fin lev|Ending Retained)', 'fsa'),
 (r'^(HPR )', 'quant'),
 (r'^(Leverage Ratio|TAKER|MAKER|Validity|Sequence of orders|Private placement|Put options|Equity swaps|Dark pools|Brokered market|Margin %)', 'equity'),
 (r'^(Alternatives|Banks|Buyout fund|Venture capital|WRAP account|Money market fund)', 'pm'),
 (r'^(Vega)', 'deriv'),
]

cards=[]
for fn, rngs in RANGES.items():
    lines=[l.rstrip('\n') for l in open(fn) if l.strip()]
    for i,l in enumerate(lines, start=1):
        if '::' not in l: continue
        term, defn = l.split('::',1)
        term, defn = term.strip(), defn.strip()
        topic='quant'
        for a,b,t in rngs:
            if a<=i<=b: topic=t
        for pat,t in OVERRIDE:
            if re.match(pat, term): topic=t; break
        cards.append({'t':term,'d':defn,'c':topic})

seen=set(); out=[]
for c in cards:
    k=(c['t'].lower(), c['d'][:40].lower())
    if k in seen: continue
    seen.add(k); out.append(c)

from collections import Counter
print(Counter(c['c'] for c in out))
print('TOTAL', len(out))
json.dump(out, open('cards.json','w'), ensure_ascii=False)

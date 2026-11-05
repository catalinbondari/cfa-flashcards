# CFA Level I practice-question pattern analysis

Built 5 Nov 2026 for the original mock exams (exam Fri 13 Nov). Data: question-level paste-ins from the main study session (`3f1f9c8f`) plus the score log and flashcard notes. All concept labels are my own paraphrases (no question text copied). Machine-readable data: `questions.json` (530 records), `blueprint.json`.

## 0. Data coverage and caveats (read first)

| Source | Questions with result | Concept known | Notes |
|---|---|---|---|
| CFA Mock A P2 (26 Oct) | 90 | 90 | Full stems + results. Session 2 topics only (Equity, FI, Deriv, Alts, PM). |
| CFA Mock A P1 | 0 | 0 | NO question-level data. Only the score (~58%) and the 41 `mk` gap cards survive; Session 1 topics (Ethics, Quant, Econ, FSA, CI) are therefore NOT covered from CFA-style mocks at all. |
| MM1 S1 (31 Oct) | 90 | 90 | Full. Q21 left blank (counted wrong). |
| MM1 S2 (31 Oct) | 90 | 90 | Full. Q20 left blank (counted wrong). |
| MM2 S1 (3 Nov) | 90 | 58 | Q33-90 full. Ethics Q1-32: only the 10 wrong numbers are known; concepts recovered for 9 of them from gap cards/assistant explanations, the 22 right ones have no concept (flagged `concept_known:false`, excluded from concept counts). |
| MM2 S2 (3 Nov) | 90 | 90 | Full (PM Q1-19 + Assets Q20-90). |
| Topic quiz M8 Hypothesis Testing (4 Nov) | 37 | 37 | Full. |
| Topic quiz M10 Simple Linear Regression (4 Nov) | 38 | 38 | Full. |
| Topic quiz M7 Long-term assets (29 Sep) | 5 | 5 | Partial: one vignette (Q9-13), results inferred from the selected/correct markers. |
| Earlier module question banks (Aug-Oct: Ethics Module 3, Equity valuation, etc.), CFA Learning Ecosystem quizzes, drills | 0 | 0 | No recoverable per-question results. Drill outcomes (Mon-Thu) are used only as qualitative error evidence in section (e). |

Totals: **530 identified questions, 530 with a known result, 508 with a known concept**. 5 full 90-question papers: only Mock A S2 is the CFA Institute's own (CFA wording). MM papers are worded differently and are harder (MM group average about 55%); treat MM miss rates as pessimistic for the real exam.

Other honest limits:
- Session-1 topic evidence rests on two MM papers (MM1 S1, MM2 S1) plus two quant topic quizzes. Session-2 topics rest on three papers. Small n per concept (most families have 2-17 items); percentages below 5 items are directional only.
- MM3 (Fri 6 Nov), CFA Mock B and C have not been taken yet; re-run this analysis after them.
- The deck's 570 base cards pre-date the mocks, so 'missed although a card existed' is true for almost every miss; the repeat-miss test in (c) therefore uses ordering across sources (a family missed, then missed again in a later paper after gap cards were made).

## (a) Scores

| Source | Score | Notes |
|---|---|---|
| CFA Mock A P2 | 52/90 (58%) | 1:54 for 90 (1:16 per question). 7 right answers were unsure guesses (Q20,30,35,47,78,86,89). |
| MM1 S1 | 39/90 (43%) | MM avg 55.4%. Full 2:15 used. |
| MM1 S2 | 42/90 (47%) | MM avg 54%. |
| MM2 S1 | 50/90 (56%) | +13 pts vs MM1 S1. Ethics 44% to 69%. |
| MM2 S2 | 49/90 (54%) | MM avg 59.7%. Section labels: PM 11/19, Assets 38/71. |
| Topic quiz M7 | 2/5 (40%) | partial vignette only |
| Topic quiz M8 | 24/37 (65%) | 53 s per question |
| Topic quiz M10 | 21/38 (55%) |  |

Paper totals: MM1 81/180 = 45%, MM2 99/180 = 55% (+10 pts). Mock A P2 58%, P1 about 58%. Trend is up but still below the 65-70% safety line on every MM paper.

### Score by topic and source

| Topic | Mock A S2 | MM1 | MM2 | Quizzes | All sources | Miss rate |
|---|---|---|---|---|---|---|
| Ethics | - | 14/32 (44%) | 22/32 (69%) | - | 36/64 (56%) | 44% |
| Quant | - | 8/15 (53%) | 6/16 (38%) | 45/75 (60%) | 59/106 (56%) | 44% |
| Econ | - | 7/11 (64%) | 8/11 (73%) | - | 15/22 (68%) | 32% |
| FSA | - | 7/21 (33%) | 10/21 (48%) | 2/5 (40%) | 19/47 (40%) | 60% |
| Corp Issuers | - | 3/11 (27%) | 5/11 (45%) | - | 8/22 (36%) | 64% |
| Equity | 15/23 (65%) | 8/23 (35%) | 12/22 (55%) | - | 35/68 (51%) | 49% |
| Fixed Income | 12/22 (55%) | 11/22 (50%) | 10/21 (48%) | - | 33/65 (51%) | 49% |
| Derivatives | 6/15 (40%) | 6/12 (50%) | 6/12 (50%) | - | 18/39 (46%) | 54% |
| Alts | 10/13 (77%) | 9/15 (60%) | 10/16 (62%) | - | 29/44 (66%) | 34% |
| Portfolio Mgmt | 9/17 (53%) | 8/18 (44%) | 10/18 (56%) | - | 27/53 (51%) | 49% |

Reading it: **Corporate Issuers (36% right) and FSA (40%) are the weakest, then Derivatives (46%); Equity, FI and PM sit near 51%; Quant and Ethics 56%; Alts (66%) and Econ (68%) are the strongest.** Ethics is the biggest weight and moved 14/32 (MM1) to 22/32 (MM2), so it is improving but is not yet safe. Quant went the other way in the MM papers (8/15 to 5/15) while the topic quizzes pulled it back to 56% overall. MM2 S2 contains one Quant item (real after-tax return) in its PM section.

## (b) Most frequently tested concepts (all sources, families of near-identical LOS)

### Top 25 overall

| # | Topic | Concept family | Items | Missed | Miss rate |
|---|---|---|---|---|---|
| 1 | Quant | hypothesis testing: Type I/II error, power, significance level | 17 | 8 | 47% |
| 2 | Equity | company/industry analysis and forecasting | 16 | 8 | 50% |
| 3 | Fixed Income | duration/convexity concepts: effective, empirical, drivers, horizon | 13 | 4 | 31% |
| 4 | Alts | real assets: real estate, REITs, infrastructure, farmland | 12 | 3 | 25% |
| 5 | Fixed Income | bond pricing: accrued interest, flat/full price, YTM, current yield | 11 | 7 | 64% |
| 6 | Alts | private equity and venture capital: LBO, exits, MOIC/IRR, co-invest | 11 | 7 | 64% |
| 7 | Quant | hypothesis tests: choose test (pooled/paired/chi-square/F) | 10 | 5 | 50% |
| 8 | Portfolio Mgmt | IPS, investor types and fund structures | 10 | 4 | 40% |
| 9 | Quant | hypothesis testing: setup of H0/Ha, test statistic, decision rule | 10 | 1 | 10% |
| 10 | FSA | long-lived assets: capitalise, impair, revalue, depreciate | 9 | 6 | 67% |
| 11 | Equity | equity indexes: weighting and return calculations | 9 | 6 | 67% |
| 12 | Equity | DDM and PV models: model selection and multistage value | 9 | 6 | 67% |
| 13 | Alts | private fund fees: hurdle, high-water mark, committed capital, FoF | 9 | 3 | 33% |
| 14 | Equity | market efficiency and anomalies | 9 | 2 | 22% |
| 15 | Quant | regression: interpret slope, intercept, dummy, functional form | 8 | 4 | 50% |
| 16 | Portfolio Mgmt | risk tolerance, risk aversion and risk objectives | 8 | 3 | 38% |
| 17 | Fixed Income | securitization: MBS, ABS, mortgages | 8 | 3 | 38% |
| 18 | Quant | regression: prediction from fitted equation and residual | 8 | 2 | 25% |
| 19 | Portfolio Mgmt | risk management and governance | 7 | 5 | 71% |
| 20 | Fixed Income | duration calculations: Macaulay, modified, approximate, portfolio, money | 7 | 5 | 71% |
| 21 | Derivatives | derivative markets, Greeks, implied volatility | 7 | 4 | 57% |
| 22 | Derivatives | option payoffs, exercise value and strategies | 7 | 4 | 57% |
| 23 | Equity | order types, trading and market structure | 7 | 4 | 57% |
| 24 | Portfolio Mgmt | portfolio risk: two-asset sigma, diversification, correlation | 7 | 3 | 43% |
| 25 | Fixed Income | bond features: callable, covenants, structures, FRNs | 6 | 4 | 67% |

### Per topic (families with at least 2 items)

**Ethics**

| Concept family | Items | Missed | Calc items |
|---|---|---|---|
| GIPS | 5 | 3 | 0 |
| Independence and objectivity I(B) | 3 | 2 | 0 |
| Suitability III(C) | 3 | 2 | 0 |
| Supervisors IV(C) | 3 | 2 | 0 |
| Market manipulation II(B) | 2 | 2 | 0 |
| Diligence V(A) | 2 | 2 | 0 |
| Performance presentation III(D) | 2 | 2 | 0 |
| Misrepresentation I(C) | 2 | 2 | 0 |
| Loyalty III(A) | 2 | 2 | 0 |
| Fair dealing III(B) | 2 | 1 | 0 |

**Quant**

| Concept family | Items | Missed | Calc items |
|---|---|---|---|
| hypothesis testing: Type I/II error, power, significance level | 17 | 8 | 1 |
| hypothesis tests: choose test (pooled/paired/chi-square/F) | 10 | 5 | 4 |
| hypothesis testing: setup of H0/Ha, test statistic, decision rule | 10 | 1 | 1 |
| regression: interpret slope, intercept, dummy, functional form | 8 | 4 | 1 |
| regression: prediction from fitted equation and residual | 8 | 2 | 7 |
| regression: assumptions, data type, causation, variables | 6 | 3 | 0 |
| parametric vs nonparametric tests | 6 | 2 | 0 |
| regression: slope significance (t-test, p-value, non-zero H0) | 5 | 3 | 2 |
| regression: R-squared, correlation from R-squared | 5 | 2 | 4 |
| covariance and correlation calculations | 5 | 1 | 3 |

**Econ**

| Concept family | Items | Missed | Calc items |
|---|---|---|---|
| FX: appreciation, cross rates, forward points, covered interest | 4 | 0 | 3 |
| fiscal policy | 3 | 1 | 0 |
| exchange rates: absorption approach and regimes | 2 | 2 | 0 |
| market structure: perfect competition, oligopoly game theory | 2 | 1 | 0 |
| monetary policy and central banks | 2 | 1 | 0 |
| geopolitics and globalization | 2 | 1 | 0 |
| business cycle phases | 2 | 1 | 0 |
| trading blocs | 2 | 0 | 0 |
| market structure: HHI and concentration | 2 | 0 | 0 |

**FSA**

| Concept family | Items | Missed | Calc items |
|---|---|---|---|
| long-lived assets: capitalise, impair, revalue, depreciate | 9 | 6 | 2 |
| deferred taxes: DTA vs DTL and permanent differences | 5 | 2 | 2 |
| financial reporting basics: audit, notes, measurement bases, CF classification | 5 | 1 | 0 |
| inventory: LIFO/FIFO, LCNRV, disclosures | 4 | 4 | 1 |
| revenue recognition | 4 | 2 | 1 |
| CFO, equity roll-forward and pro forma modelling | 4 | 2 | 4 |
| ratio analysis: common-size, quick, solvency | 3 | 1 | 2 |
| diluted EPS | 2 | 2 | 2 |
| FCFF and FCFE | 2 | 2 | 2 |
| goodwill and acquisition accounting | 2 | 2 | 0 |

**Corp Issuers**

| Concept family | Items | Missed | Calc items |
|---|---|---|---|
| capital allocation: NPV, IRR, ROIC and market reaction | 5 | 2 | 2 |
| liquidity: sources, drags/pulls, cash conversion cycle | 4 | 3 | 1 |
| governance and agency costs | 2 | 2 | 0 |
| real options | 2 | 2 | 0 |
| public vs private issuers and taxation | 2 | 2 | 1 |
| capital structure theory | 2 | 1 | 0 |
| business models | 2 | 1 | 0 |
| WACC and cost of capital | 2 | 1 | 1 |

**Equity**

| Concept family | Items | Missed | Calc items |
|---|---|---|---|
| company/industry analysis and forecasting | 16 | 8 | 4 |
| equity indexes: weighting and return calculations | 9 | 6 | 3 |
| DDM and PV models: model selection and multistage value | 9 | 6 | 5 |
| market efficiency and anomalies | 9 | 2 | 0 |
| order types, trading and market structure | 7 | 4 | 0 |
| P/E multiples, justified P/E, sustainable growth | 6 | 2 | 3 |
| margin buying and leverage ratio | 5 | 1 | 5 |
| preference shares | 3 | 0 | 0 |
| dividends: stock dividend vs cash | 2 | 2 | 0 |
| ADRs and global shares | 2 | 2 | 0 |

**Fixed Income**

| Concept family | Items | Missed | Calc items |
|---|---|---|---|
| duration/convexity concepts: effective, empirical, drivers, horizon | 13 | 4 | 0 |
| bond pricing: accrued interest, flat/full price, YTM, current yield | 11 | 7 | 10 |
| securitization: MBS, ABS, mortgages | 8 | 3 | 0 |
| duration calculations: Macaulay, modified, approximate, portfolio, money | 7 | 5 | 7 |
| bond features: callable, covenants, structures, FRNs | 6 | 4 | 1 |
| credit analysis and ratings | 6 | 2 | 2 |
| sovereign and government debt issuance | 5 | 1 | 0 |
| yield spreads: G-, Z-, I-spread, credit spreads | 4 | 2 | 1 |
| spot and forward rates | 2 | 2 | 2 |
| repo | 2 | 1 | 1 |

**Derivatives**

| Concept family | Items | Missed | Calc items |
|---|---|---|---|
| derivative markets, Greeks, implied volatility | 7 | 4 | 0 |
| option payoffs, exercise value and strategies | 7 | 4 | 5 |
| forward valuation and arbitrage | 6 | 3 | 2 |
| forwards vs futures | 6 | 2 | 2 |
| swaps | 4 | 2 | 0 |
| put-call-forward parity | 3 | 3 | 2 |
| binomial option model | 3 | 2 | 2 |
| option value bounds | 3 | 1 | 3 |

**Alts**

| Concept family | Items | Missed | Calc items |
|---|---|---|---|
| real assets: real estate, REITs, infrastructure, farmland | 12 | 3 | 0 |
| private equity and venture capital: LBO, exits, MOIC/IRR, co-invest | 11 | 7 | 0 |
| private fund fees: hurdle, high-water mark, committed capital, FoF | 9 | 3 | 6 |
| hedge funds: strategies, lockups, prime broker | 5 | 0 | 0 |
| digital assets | 4 | 1 | 0 |
| private debt | 2 | 1 | 0 |

**Portfolio Mgmt**

| Concept family | Items | Missed | Calc items |
|---|---|---|---|
| IPS, investor types and fund structures | 10 | 4 | 0 |
| risk tolerance, risk aversion and risk objectives | 8 | 3 | 1 |
| risk management and governance | 7 | 5 | 0 |
| portfolio risk: two-asset sigma, diversification, correlation | 7 | 3 | 2 |
| behavioral finance and anomalies | 6 | 3 | 0 |
| CAPM/SML: expected return and valuation | 6 | 3 | 5 |
| CAL/CML, Sharpe ratio and optimal portfolio, M-squared | 6 | 2 | 5 |
| beta calculation | 3 | 3 | 3 |

Structural facts that matter for mock design (from the MM LOS tags, 325 items):
- Ethics (MM1 S1, the only paper with LOS tags): 21 of 32 items sit on LM2 (Code and Standards), 8 on LM3 (application), 3 on LM4 (GIPS); LM1 never appeared. In the exam about one question in three is Ethics, so expect Standards-by-Standards scenario questions.
- Quant items concentrate in LM8-LM10 (hypothesis testing, nonparametric tests, regression): 11 of 31 MM Quant items, plus 75 quiz items on M8 and M10.
- Fixed Income: LM3 (issuance and trading) never appeared; LM2 (cash-flow structures) appeared 7 times with 6 misses.
- Equity LM8 (valuation) is the heaviest single LM (10 items, 7 missed).

## (c) Weakest concepts

### Ranked by miss count (families with at least 4 items and 45%+ missed, or 100% missed with 2+ items)

| Topic | Concept family | Missed/items | Sources missed in | Missed again later? |
|---|---|---|---|---|
| Equity | company/industry analysis and forecasting | 8/16 | MM1 S2, MM2 S2 | YES |
| Quant | hypothesis testing: Type I/II error, power, significance level | 8/17 | MM2 S1, Topic quiz M8 | YES |
| Fixed Income | bond pricing: accrued interest, flat/full price, YTM, current yield | 7/11 | CFA Mock A P2, MM1 S2, MM2 S2 | YES |
| Alts | private equity and venture capital: LBO, exits, MOIC/IRR, co-invest | 7/11 | CFA Mock A P2, MM1 S2, MM2 S2 | YES |
| FSA | long-lived assets: capitalise, impair, revalue, depreciate | 6/9 | Topic quiz M7, MM1 S1, MM2 S1 | YES |
| Equity | equity indexes: weighting and return calculations | 6/9 | CFA Mock A P2, MM1 S2, MM2 S2 | YES |
| Equity | DDM and PV models: model selection and multistage value | 6/9 | CFA Mock A P2, MM1 S2, MM2 S2 | YES |
| Portfolio Mgmt | risk management and governance | 5/7 | CFA Mock A P2, MM1 S2, MM2 S2 | YES |
| Fixed Income | duration calculations: Macaulay, modified, approximate, portfolio, money | 5/7 | CFA Mock A P2, MM1 S2, MM2 S2 | YES |
| Quant | hypothesis tests: choose test (pooled/paired/chi-square/F) | 5/10 | Topic quiz M8 | no |
| FSA | inventory: LIFO/FIFO, LCNRV, disclosures | 4/4 | MM1 S1, MM2 S1 | YES |
| Fixed Income | bond features: callable, covenants, structures, FRNs | 4/6 | MM1 S2, MM2 S2 | YES |
| Derivatives | derivative markets, Greeks, implied volatility | 4/7 | CFA Mock A P2, MM1 S2, MM2 S2 | YES |
| Derivatives | option payoffs, exercise value and strategies | 4/7 | CFA Mock A P2, MM2 S2 | YES |
| Equity | order types, trading and market structure | 4/7 | CFA Mock A P2, MM1 S2, MM2 S2 | YES |
| Quant | regression: interpret slope, intercept, dummy, functional form | 4/8 | MM1 S1, MM2 S1, Topic quiz M10 | YES |
| Derivatives | put-call-forward parity | 3/3 | CFA Mock A P2, MM1 S2, MM2 S2 | YES |
| Portfolio Mgmt | beta calculation | 3/3 | MM2 S2 | no |
| Corp Issuers | liquidity: sources, drags/pulls, cash conversion cycle | 3/4 | MM1 S1, MM2 S1 | YES |
| Quant | descriptive statistics: dispersion, mean types, skew/kurtosis | 3/4 | MM2 S1 | no |
| Ethics | GIPS | 3/5 | MM1 S1, MM2 S1 | YES |
| Quant | regression: slope significance (t-test, p-value, non-zero H0) | 3/5 | Topic quiz M10 | no |
| Portfolio Mgmt | behavioral finance and anomalies | 3/6 | MM1 S2, MM2 S2 | YES |
| Portfolio Mgmt | CAPM/SML: expected return and valuation | 3/6 | CFA Mock A P2, MM1 S2 | YES |
| Derivatives | forward valuation and arbitrage | 3/6 | CFA Mock A P2, MM1 S2, MM2 S2 | YES |
| Quant | regression: assumptions, data type, causation, variables | 3/6 | Topic quiz M10 | no |
| Ethics | Market manipulation II(B) | 2/2 | MM1 S1 | no |
| Ethics | Diligence V(A) | 2/2 | MM1 S1, MM2 S1 | YES |
| Ethics | Performance presentation III(D) | 2/2 | MM1 S1, MM2 S1 | YES |
| Ethics | Misrepresentation I(C) | 2/2 | MM1 S1 | no |
| Ethics | Loyalty III(A) | 2/2 | MM1 S1, MM2 S1 | YES |
| FSA | diluted EPS | 2/2 | MM1 S1, MM2 S1 | YES |
| Corp Issuers | governance and agency costs | 2/2 | MM1 S1, MM2 S1 | YES |
| Corp Issuers | real options | 2/2 | MM1 S1, MM2 S1 | YES |
| FSA | FCFF and FCFE | 2/2 | MM1 S1, MM2 S1 | YES |
| Econ | exchange rates: absorption approach and regimes | 2/2 | MM1 S1, MM2 S1 | YES |
| FSA | goodwill and acquisition accounting | 2/2 | MM1 S1 | no |
| Corp Issuers | public vs private issuers and taxation | 2/2 | MM1 S1 | no |
| Quant | correlation significance t-test (Pearson, Spearman) | 2/2 | MM1 S1, MM2 S1 | YES |
| Equity | dividends: stock dividend vs cash | 2/2 | CFA Mock A P2, MM1 S2 | YES |
| Equity | ADRs and global shares | 2/2 | MM1 S2, MM2 S2 | YES |
| Fixed Income | spot and forward rates | 2/2 | MM1 S2, MM2 S2 | YES |
| Quant | regression: prediction interval and forecast interval | 2/2 | Topic quiz M10 | no |
| Quant | time value / interest rates: building blocks, real returns | 2/4 | MM1 S1, MM2 S1 | YES |
| FSA | revenue recognition | 2/4 | MM1 S1, MM2 S1 | YES |
| FSA | CFO, equity roll-forward and pro forma modelling | 2/4 | MM2 S1 | no |
| Derivatives | swaps | 2/4 | CFA Mock A P2, MM2 S2 | YES |
| Fixed Income | yield spreads: G-, Z-, I-spread, credit spreads | 2/4 | CFA Mock A P2, MM1 S2 | YES |

### Repeat misses: the same skill tested again in a later paper (item level)

`w` = wrong, `r` = right. Order = date taken. **(repeat miss)** = wrong at least twice, i.e. missed again after its gap card existed (cards were made right after each paper).

| Skill | Results in order |
|---|---|
| Put-call / put-call-forward parity **(repeat miss)** | Mock A S2 Q23 w, MM1 S2 Q57 w, MM2 S2 Q48 w |
| Inventory methods (LIFO/FIFO/LCNRV/disclosure) **(repeat miss)** | MM1 S1 Q39 w, MM1 S1 Q43 w, MM2 S1 Q35 w, MM2 S1 Q58 w |
| Real options: identify the option **(repeat miss)** | MM1 S1 Q46 w, MM2 S1 Q70 w |
| Diluted EPS **(repeat miss)** | MM1 S1 Q38 w, MM2 S1 Q77 w |
| FCFF / FCFE **(repeat miss)** | MM1 S1 Q48 w, MM2 S1 Q41 w |
| Implied spot rate from forward rates **(repeat miss)** | MM1 S2 Q87 w, MM2 S2 Q80 w |
| Bond pricing: accrued interest, flat price, current yield **(repeat miss)** | MM1 S2 Q62 r, MM1 S2 Q77 w, MM2 S2 Q36 w, MM2 S2 Q90 w |
| Duration / convexity calculations **(repeat miss)** | Mock A S2 Q20 r, Mock A S2 Q26 w, Mock A S2 Q34 w, MM1 S2 Q23 r, MM1 S2 Q54 w, MM1 S2 Q55 w, MM2 S2 Q49 w |
| Total return / price index mechanics **(repeat miss)** | Mock A S2 Q27 w, MM1 S2 Q48 w, MM2 S2 Q42 w, MM2 S2 Q47 r |
| Stock dividend vs cash dividend **(repeat miss)** | Mock A S2 Q66 w, MM1 S2 Q22 w |
| ADR / global registered share types **(repeat miss)** | MM1 S2 Q36 w, MM2 S2 Q68 w |
| Soft vs hard hurdle in fees **(repeat miss)** | Mock A S2 Q2 r, MM1 S2 Q38 w, MM2 S2 Q44 w |
| Private equity: buyout, exit, MOIC vs IRR **(repeat miss)** | Mock A S2 Q64 w, MM1 S2 Q86 w, MM2 S2 Q61 w, MM2 S2 Q69 w, MM2 S2 Q41 w |
| Risk budgeting / risk management process **(repeat miss)** | Mock A S2 Q11 w, MM1 S2 Q1 w, MM2 S2 Q8 w, MM2 S2 Q9 w |
| Beta (Cov/var, rho*sigma ratio) and CAPM **(repeat miss)** | Mock A S2 Q17 w, MM2 S2 Q3 w, MM2 S2 Q5 w, MM2 S2 Q14 w |
| DDM: multistage and model selection **(repeat miss)** | Mock A S2 Q52 w, MM1 S2 Q39 w, MM1 S2 Q67 w, MM1 S2 Q88 w, MM2 S2 Q53 w, MM2 S2 Q64 r |
| Justified / forward P/E **(repeat miss)** | Mock A S2 Q77 r, MM1 S2 Q40 w, MM2 S1 Q57 w, MM2 S2 Q34 w, MM2 S2 Q73 r |
| Type I / Type II / power / significance **(repeat miss)** | MM1 S1 Q89 r, MM2 S1 Q51 w, MM2 S1 Q54 r, MM2 S1 Q62 w, M8 Q8 w, M8 Q9 w, M8 Q21 w, M8 Q30 w |
| Nonparametric / Spearman / correlation test **(repeat miss)** | MM1 S1 Q33 w, MM1 S1 Q75 w, MM2 S1 Q44 w, M8 Q29 w |
| Liquidity: pulls, drags, factoring, CCC **(repeat miss)** | MM1 S1 Q54 w, MM2 S1 Q45 w, MM2 S1 Q53 w |
| Revenue recognition **(repeat miss)** | MM1 S1 Q58 w, MM1 S1 Q74 r, MM2 S1 Q47 r, MM2 S1 Q71 w |
| Capitalised interest / borrowing costs **(repeat miss)** | M7 Q9 w, MM2 S1 Q74 w |
| Governance / agency costs **(repeat miss)** | MM1 S1 Q40 w, MM2 S1 Q34 w |
| Absorption approach / exchange-rate regime **(repeat miss)** | MM1 S1 Q52 w, MM2 S1 Q72 w |
| Deferred tax **(repeat miss)** | MM1 S1 Q50 r, MM1 S1 Q63 w, MM1 S1 Q66 w, MM2 S1 Q39 r, MM2 S1 Q60 r |
| Margin buying (fixed) | Mock A S2 Q48 w, MM1 S2 Q35 r, MM1 S2 Q81 r, MM2 S2 Q52 r |
| Binomial hedge ratio (fixed) | MM1 S2 Q50 w, MM2 S2 Q35 r |
| Semi-strong efficiency / EMH **(repeat miss)** | Mock A S2 Q59 w, MM1 S2 Q41 w, MM2 S2 Q78 r, MM2 S2 Q59 r |
| Behavioral biases **(repeat miss)** | MM1 S2 Q6 w, MM1 S2 Q16 w, MM2 S2 Q2 w, MM2 S2 Q17 r, Mock A S2 Q70 r |
| Forward value / arbitrage direction **(repeat miss)** | Mock A S2 Q21 w, MM1 S2 Q69 w, MM2 S2 Q83 w, MM1 S2 Q31 r |
| Yield spreads (G, Z, I) **(repeat miss)** | Mock A S2 Q71 w, MM1 S2 Q24 w, MM2 S2 Q28 r |
| Regression ANOVA F / R2 **(repeat miss)** | MM1 S1 Q90 w, M10 Q26 w, M10 Q35 w, M10 Q9 r |
| Ethics: GIPS **(repeat miss)** | MM1 S1 Q24 w, MM1 S1 Q25 r, MM1 S1 Q32 r, MM2 S1 Q13 w, MM2 S1 Q18 w |
| Ethics: Supervisors IV(C) **(repeat miss)** | MM1 S1 Q26 r, MM1 S1 Q31 w, MM2 S1 Q1 w |
| Ethics: Independence I(B) **(repeat miss)** | MM1 S1 Q4 w, MM1 S1 Q10 r, MM2 S1 Q23 w |
| Ethics: Suitability III(C) **(repeat miss)** | MM1 S1 Q16 w, MM1 S1 Q17 r, MM2 S1 Q4 w |
| Ethics: Performance presentation III(D) **(repeat miss)** | MM1 S1 Q5 w, MM2 S1 Q10 w |
| Ethics: Diligence V(A) **(repeat miss)** | MM1 S1 Q2 w, MM2 S1 Q14 w |
| Ethics: Loyalty III(A) **(repeat miss)** | MM1 S1 Q21 w, MM2 S1 Q28 w |

What this says:
- **Never fixed after a card:** put-call(-forward) parity (0/3), inventory methods (0/4), diluted EPS (0/2), FCFF/FCFE (0/2), real options (0/2), implied spot rates (0/2), stock dividend (0/2), ADR types (0/2), total-return index mechanics (1/4 right), soft vs hard hurdle comparison (0/2), private-equity exits/MOIC (0/5), risk management/budgeting (0/4), liquidity pulls and drags (0/3), governance/agency (0/2), absorption approach (0/2), capitalised interest (0/2), beta (0/3 in MM2, then a lesson and 3/3 in the drill).
- **Fixed after a card (keep as retention checks, not priorities):** margin buying (Mock A wrong, then 3 right), binomial hedge ratio (wrong then right), semi-strong efficiency (wrong twice, then right twice in MM2), yield spreads (wrong twice, right at MM2 S2 Q28), deferred tax direction (3 right of 5, but drills still failing, so not safe).
- Gap-card pass rates (from the log): Mock A cards first pass 10 got / 20 missed (first 30), MM1 gap cards 53/104 got (51%), MM2 gap cards 58/88 (66%), re-pass of the 30 missed MM2 cards 22/30 (73%). About half of the cards built from his own mistakes are still failed on first recall.

### Top 15 weakest concepts (use these first)

1. Put-call and put-call-forward parity (0/3; sign and spot vs forward)
2. Inventory: LIFO/FIFO/LCNRV/liquidation (0/4)
3. Type I/II error, power and significance wording (8/17 missed; M8 5/9 of the wording set)
4. Diluted EPS (0/2 in mocks; drills only reached 5/7 after fixes)
5. FCFF/FCFE (0/2; payables sign slip repeated in drills)
6. Deferred taxes: DTA vs DTL for liabilities, difference x rate, tax expense signs (2/5 missed in mocks; Tue, Wed and Thu drills each 1/3)
7. Duration calculations: portfolio (MV weights), Macaulay, approximate, annualisation (5/7)
8. Bond pricing: accrued interest, flat price, current yield, BA II Plus BOND inputs (7/11)
9. Equity indexes: price vs total return, weighting, return (6/9)
10. DDM: multistage (D_n+1 at year n) and model selection (6/9)
11. Beta from Cov/sigma_m^2 and rho x sigma_i/sigma_m, then CAPM (3/3 in MM2)
12. Regression: prediction interval x t_c, SEE with n-2, un-log, non-zero H0 (11/21)
13. Risk management process, risk budgeting, governance (5/7)
14. Private equity: exits, buyouts, MOIC vs IRR, clawback (7/11)
15. Long-lived assets: capitalised interest, impairment, revaluation effects on ratios (6/9)

Other weak clusters just outside the 15: real options (0/2), liquidity pulls vs drags (3/4), Ethics standards GIPS (3/5), I(B) gifts (2/3), IV(C) supervisors (2/3), III(C) suitability (2/3), nonparametric/Spearman (4/8), company/industry analysis and forecasting (8/16), stock dividends and ADRs (0/4 combined), behavioral bias classification (3/6).

## (d) Calculation vs concept miss rates

`calc` = the answer requires working out a number (heuristic: all three options numeric, hand-corrected). 146 calc items, 384 concept items.

| Topic | Calc items | Calc miss rate | Concept items | Concept miss rate |
|---|---|---|---|---|
| Ethics | 0 | - | 64 | 44% |
| Quant | 38 | 47% | 68 | 43% |
| Econ | 3 | 0% | 19 | 37% |
| FSA | 18 | 61% | 29 | 59% |
| Corp Issuers | 5 | 80% | 17 | 59% |
| Equity | 20 | 60% | 48 | 44% |
| Fixed Income | 24 | 67% | 41 | 39% |
| Derivatives | 16 | 56% | 23 | 52% |
| Alts | 6 | 33% | 38 | 34% |
| Portfolio Mgmt | 16 | 56% | 37 | 46% |
| **All** | 146 | **55%** | 384 | **44%** |

Calc questions are missed more often (55% vs 44%). The gap is biggest in **Fixed Income (67% vs 39%)** and **Equity (60% vs 44%)**; CI calc is 4/5 missed (tiny n). In Quant and Derivatives the two are close, which means Quant misses are about the method/wording, not arithmetic. Ethics has no calc. Alts and Econ miss rates are low in both.

Wording effect: items whose stem asks for the **least/not/incorrect/inaccurate** option are missed **64%** (60/94) vs **46%** for positively worded stems (190/413). The MM2 S1 Ethics stems are not available and are excluded here.

## (e) Recurring error types

Evidence is the 530 items plus the assistant's walk-throughs and Mon-Thu drills in the study transcript.

**1. Sign and direction flips**
- FCFE/FCFF: liability increase must be plus, asset increase minus. The payables sign slip was repeated across the Tue and Wed drills.
- Put-call-forward parity written as p - c instead of c - p, and spot used where the forward belongs (Mock A Q23, MM1 S2 Q57, MM2 S2 Q48).
- Income tax expense = payable + change in DTL - change in DTA: a falling DTL treated as a rise (Thu drill, 305 vs 285). DTA/DTL direction flipped for a warranty liability (twice in drills).
- Negative X change in a regression (M10 Q14); negative covariance gives negative r and negative t, so do not reject in a right-tail test (MM2 S1 Q44).
- Direction of explanation: which variable explains which (M10 Q15, Q22).

**2. Last step skipped or an input slot wrong**
- Prediction interval: left off the x t_c (M10 Q28, Q34). Log-linear model: forgot e^x (Q38). SEE: divided by n instead of n - 2 (Q31). F-stat: forgot to divide by degrees of freedom (MM1 S1 Q90: trap answer 1 = SSR/SSE, correct 20).
- Multistage DDM: used D_n instead of D_n+1 in the terminal Gordon step, placed it one year late, or forgot to add D_n in the same year (Mock A Q52; drills on 28 Oct and 2 Nov).
- Diluted EPS: added interest x t instead of x (1 - t); added interest but forgot the new shares; mishandled preferred dividends: non-convertible must be subtracted from the numerator, convertible added back (MM1 S1 Q38, MM2 S1 Q77).
- Portfolio duration weighted by par instead of market value (MM1 S2 Q54). WACC: given D/E, must convert to weights first and use the marginal tax rate (MM1 S1 Q56). Two-asset sigma: dropped the 2 in the cross term, or unsquared weights (Mock A Q42). Beta: forgot to square the market sigma, flipped which sigma is on top (MM2 S2 Q3,5,14). Sample vs population SD in the CV (drill).
- Pooled t: used the mean as the SD, divided by n^2, forgot the root; all three slips on one question (drill).

**3. Wording traps**
- Type I/II/power: the wrong option copies the correct wording and swaps one noun ('true alternative hypothesis'); 'exceeds the critical value' paired with 'accept H0' (M8 Q22). Rule that worked: errors are always about H0, read the last word.
- 'Least accurate/least likely/not' stems: 64% missed vs 46% otherwise. Examples: ABS asset/liability swap (MM2 S2 Q55), value chain vs supply chain (MM2 S1 Q37).
- Look-alike concepts: cognitive vs emotional biases, momentum is still an anomaly even when biases explain it (MM2 S2 Q2), VaR is not the worst-case loss, cluster vs stratified sampling (read the final step), Eurobond vs foreign bond, customs union vs free trade area, MOIC ignores time, retractable vs callable preferred, 'cumulative' vs 'participating'.
- Distractor data: the risk-free rate in CAL slope questions, the coupon and yield columns in a pre-built duration table, 'maturity' vs 'tenor' for N in YTM (MM2 S2 Q90), the convertible preferred that cannot convert.

**4. Calculator and input errors**
- BA II Plus BOND worksheet (8/12): all four misses were inputs (RDT month, RDT year +1, SDT year, RV entered as 100 instead of the call price); EUR date format must be kept consistent.
- Chain-mode arithmetic in pooled variance (9 x 4 + 11 x 9 gives 423 without brackets), rounding before STO, 30/360 vs ACT day counts, BEY vs EAR (picked the compounded answer).

**5. Choosing the wrong model/test**
- Chi-square (one variance) vs F (two variances) vs t (means) (M8 Q16,17,26,29). Which DDM (past slow growth does not make it multistage, MM1 S2 Q88). Real options: calling a fundamental option a call option on the commodity (MM1 S1 Q46). Which duration (effective for embedded options, money duration units).

**6. Cards do not stick / process**
- Misses on concepts already on cards: FCFF (MM1 S1 Q48), permanent difference (Q63), Spearman (Q75), F-stat (Q90), lognormal (Q34), nonparametric (Q33); on MM1 S2: risk budgeting, relative risk objective, stock dividend, Z vs G spread, semi-strong, total return index, put-call-forward parity. Cause logged in the plan: gap cards not yet studied before the next paper.
- Two questions left blank (MM1 S1 Q21, MM1 S2 Q20). Seven Mock A answers were right but unsure, so the true score of the weak areas is a little lower than the headline.
- Pace is not the problem: Mock A 1:16 per question, MM papers 2:14-2:15 used in full. The losses are method and reading errors.

## (f) Blueprint for ONE original 180-question mock (2 x 90)

Topic counts (official 2026 weight ranges converted to questions of 180) with the tilt toward weak topics:

| Session | Topic | Weight range | Questions | Share | Why this count |
|---|---|---|---|---|---|
| 1 | Ethics | 15-20% (27-36) | **31** | 17.2% | Largest weight, 56% right and MM2 only 69%; upper-middle of range |
| 1 | Quant | 6-9% (11-16) | **12** | 6.7% | Mid-range; method and wording misses, not arithmetic |
| 1 | Econ | 6-9% (11-16) | **11** | 6.1% | Strongest topic (68%); at the minimum |
| 1 | FSA | 11-14% (20-25) | **23** | 12.8% | Second-weakest (40%); upper range |
| 1 | Corp Issuers | 6-9% (11-16) | **13** | 7.2% | Weakest topic (36%) but only 6-9% weight; upper-middle |
| 2 | Equity | 11-14% (20-25) | **23** | 12.8% | 51%, many repeat-miss families; mid-upper |
| 2 | Fixed Income | 11-14% (20-25) | **22** | 12.2% | 51%, calc miss rate 67%; mid |
| 2 | Derivatives | 5-8% (9-14) | **14** | 7.8% | 46%, parity never fixed; top of range |
| 2 | Alts | 7-10% (13-18) | **13** | 7.2% | 66%; near minimum |
| 2 | Portfolio Mgmt | 8-12% (14-22) | **18** | 10.0% | 51%; beta and risk management repeats; mid-upper |

Session 1 = 90 (Ethics 31, Quant 12, Econ 11, FSA 23, CI 13). Session 2 = 90 (Equity 23, FI 22, Deriv 14, Alts 13, PM 18). All 10 topics sit inside the official ranges.

Rules for question writers:
- Within each topic about 70% of items are 'frequent' or 'weak' concepts, about 30% 'coverage' (LOS he has barely or never been tested on).
- Mix style per topic using the table below: keep the calc share near the observed share but over-weight calc in FI and Equity (miss rates 67% and 60%).
- Build in the observed traps: about 1 in 6 stems 'least/not'; distractors that are the classic slip answer (no sqrt, n not n-2, D_n not D_n+1, par weights, sign flip).
- Order inside a session like the real exam: Session 1 Ethics, Quant, Econ, FSA, CI; Session 2 Equity, FI, Deriv, Alts, PM.

### Session 1 - Ethics (31 questions)

| Concept to test | Qs | Why | Evidence | Style |
|---|---|---|---|---|
| GIPS: composites, who may claim compliance, firm definition, requirements | 3 | weak | missed 3/5 across MM1, MM2 (composites, consultants, total firm assets) | concept |
| Independence and objectivity I(B): gifts, issuer-paid research and travel | 2 | weak | missed 2/3 (gift, travel) | concept |
| Suitability III(C): know the client, judge in portfolio context | 2 | weak | missed 2/3 | concept |
| Supervisors IV(C): inadequate compliance, suspected violation | 2 | weak | missed 2/3 (restrict and monitor, not just warn) | concept |
| Conflicts VI(A) and referral fees VI(C): what and when to disclose | 2 | frequent | VI(C) wrong; VI(A) 2 right; "must disclose" minimum-answer trap | concept |
| Diligence V(A) and communication V(B): research depth, fact vs forecast | 2 | weak | missed 2/2 diligence | concept |
| Performance presentation III(D): TWR vs MWR, composites in marketing | 1 | weak | missed 2/2 | concept |
| Loyalty, prudence and care III(A): proxy voting, who is the client | 1 | weak | missed 2/2 (one left blank) | concept |
| Market manipulation II(B) and MNPI II(A) | 2 | weak | missed 3/3 (info-based vs transaction-based; public info) | concept |
| Misrepresentation I(C) and misconduct I(D) | 2 | weak | missed 3/3 | concept |
| Fair dealing III(B) and priority of transactions VI(B) | 2 | weak | missed 2/3 (changed recommendation, family accounts) | concept |
| Record retention V(C) and prior-employer work product | 1 | weak | missed 1/2 | concept |
| Loyalty to employer IV(A): whistleblowing, non-compete, independent practice | 2 | coverage | IV(A) never tested | concept |
| Ethics foundations: Code of Ethics, professionalism, ethical decision framework | 2 | coverage | LM1 never tested (MM data only LM2-4) | concept |
| Confidentiality III(E) exceptions and Knowledge of law I(A) | 2 | coverage | tested 1x each, right | concept |
| GIPS: verification, presentation and asset-owner basics | 1 | coverage | LM4 only 3 Qs seen | concept |
| CFA Program conduct VII(A)/(B): designation claims | 1 | coverage | 2/2 right but only 2 items | concept |
| Additional compensation IV(B) and responsibilities to employer | 1 | coverage | 1 right, 1 missed (firm policy vs Code) | concept |

Subtotal: 22 frequent/weak + 9 coverage = 31 (71% / 29%).

### Session 1 - Quant (12 questions)

| Concept to test | Qs | Why | Evidence | Style |
|---|---|---|---|---|
| Hypothesis testing: Type I/II error, power, significance level wording | 1 | weak | missed 8/17 (M8 Q6,8,9,21,30; MM2 S1 Q51,62) | concept |
| Test selection and calc: pooled t, paired t, chi-square single variance, F-test | 1 | weak | missed 5/10; pooled t 1/3 in drill | calc |
| Regression: prediction interval (x t_c), SEE (n-2), un-log, forecast from equation | 2 | weak | missed prediction interval 2/2, SEE 1/3, log-linear 1/1 | calc |
| Regression: ANOVA F, R-squared vs r, slope t-test against non-zero H0, dummy interpretation | 1 | weak | missed 11/21 across M10, MM1, MM2 | calc |
| Parametric vs nonparametric; Spearman rank correlation and correlation t-test | 1 | weak | missed 4/8 (MM1 Q33,Q75; MM2 Q44; M8 Q29) | concept |
| Descriptive statistics: CV, sample vs population SD, harmonic/geometric mean, downside deviation | 1 | weak | missed 3/4; downside dev 0/1, CV 2/2 in drills | calc |
| Covariance, correlation and expected value/variance from probability tables | 1 | frequent | 7 items, 2 missed (MM1 S1 Q42 sigma) | calc |
| Time value of money: annuities, EAR, loan amortisation | 1 | coverage | LM2 only 2 Qs seen | calc |
| Probability: Bayes, total probability, counting rules, probability trees | 1 | coverage | LM4 barely tested | concept |
| Confidence intervals, standard error, t vs z, degrees of freedom | 1 | coverage | SE quadruple-n drill 1/2 | calc |
| Simulation and lognormal; Big Data and ML terminology | 1 | coverage | lognormal missed 1/1; ML 1/2 | concept |

Subtotal: 8 frequent/weak + 4 coverage = 12 (67% / 33%).

### Session 1 - Econ (11 questions)

| Concept to test | Qs | Why | Evidence | Style |
|---|---|---|---|---|
| FX calculations: cross rates, forward points, triangular arbitrage, appreciation vs depreciation | 2 | frequent | 4 items, all right but exam-critical calc | calc |
| Exchange-rate regimes and trade-balance effects (absorption, Marshall-Lerner) | 1 | weak | missed 2/2 | concept |
| Fiscal policy: multiplier, crowding out, automatic stabilisers | 1 | frequent | missed 1/3 | concept |
| Monetary policy: tools, neutral rate, central bank roles and independence | 1 | frequent | missed 1/2 | concept |
| Business cycle phases and indicators | 1 | frequent | missed 1/2 (late expansion) | concept |
| Market structures: HHI, Nash equilibrium, long-run competition | 1 | frequent | missed 1/4 | concept |
| Geopolitics, globalisation, trading blocs | 1 | frequent | missed 1/4 | concept |
| Comparative advantage, tariffs, quotas, trade restrictions | 1 | coverage | LM6 sparsely tested | concept |
| Elasticity, breakeven and shutdown points, monopoly and monopolistic competition | 1 | coverage | LM1 identification items only | concept |
| Balance of payments and capital flows | 1 | coverage | not tested | concept |

Subtotal: 8 frequent/weak + 3 coverage = 11 (73% / 27%).

### Session 1 - FSA (23 questions)

| Concept to test | Qs | Why | Evidence | Style |
|---|---|---|---|---|
| Deferred taxes: DTA vs DTL (incl. liabilities), difference x rate, tax expense sign rule | 3 | weak | missed 2/5 in mocks; drills 1/3 (Tue), 1/3 (Wed), 1/3 (Thu) then 2/3 retest with DTL-fall sign slip | calc |
| Diluted EPS: convertible bonds/preferred, options (TSM), antidilution | 2 | weak | missed 2/2 in mocks; drills 0/3, 2/2, 4/6, then 5/7 | calc |
| FCFF and FCFE from NI/CFO (payables sign, Int(1-t), net borrowing) | 2 | weak | missed 2/2; payables sign slip repeated across Tue and Wed drills | calc |
| Long-lived assets: capitalised interest, impairment, revaluation, depreciation effects on ratios | 2 | weak | missed 6/9 | concept |
| Inventory: LIFO vs FIFO vs weighted average, LIFO liquidation, LCNRV US GAAP vs IFRS | 2 | weak | missed 4/4 | concept |
| Revenue recognition: percentage of completion, bill-and-hold, contract steps | 1 | weak | missed 2/4 | calc |
| DuPont, ROE vs required return, sustainable growth | 1 | frequent | missed 1/2; ROE drill 2/3 | calc |
| Pro forma modelling, CFO indirect method and equity roll-forward | 1 | frequent | 4 items, 2 missed (equity roll-forward, CFO) | calc |
| Leases (lessee view) and long-term liabilities | 1 | weak | leases missed 1/2 | concept |
| Pensions: DB assumptions, OCI vs P&L | 1 | frequent | missed 1/2 | concept |
| Bond issuance, effective interest amortisation, debt covenants (long-term liabilities) | 1 | coverage | LM7 not tested as a calc | calc |
| Income statement: non-recurring items, discontinued ops, OCI, comprehensive income | 1 | coverage | LM2 only revenue items tested | concept |
| Cash flow statement: direct method, IFRS vs US GAAP classification | 1 | coverage | 1 item seen | concept |
| Financial reporting quality: earnings quality spectrum, warning signs | 1 | coverage | 1 item seen (missed) | concept |
| Activity and liquidity ratios: DSO, DIO, turnover, cash conversion cycle calc | 1 | coverage | ratio calcs seen as quick ratio only | calc |
| Balance sheet: intangibles, goodwill impairment, equity components, treasury stock | 1 | coverage | goodwill missed 2/2; treasury roll-forward missed | concept |
| Expense recognition: depreciation methods, warranties, bad debts | 1 | coverage | depreciation calc not tested | calc |

Subtotal: 16 frequent/weak + 7 coverage = 23 (70% / 30%).

### Session 1 - Corp Issuers (13 questions)

| Concept to test | Qs | Why | Evidence | Style |
|---|---|---|---|---|
| Real options: identify timing, sizing, abandonment, flexibility, fundamental options | 1 | weak | missed 2/2 | concept |
| Capital allocation: NPV vs IRR conflicts, ROIC vs WACC, share-price NPV, project categories | 2 | weak | missed 2/5 | calc |
| WACC with target D/E weights, marginal tax, project risk adjustment | 1 | weak | missed 1/2; D/E to weights trap | calc |
| Liquidity: primary vs secondary sources, drags vs pulls, factoring, cash conversion cycle | 2 | weak | missed 3/4 | concept |
| Governance and agency: stakeholder vs shareholder theory, pay structures | 1 | weak | missed 2/2 | concept |
| Capital structure: static trade-off, why leverage below optimum, start-up financing | 1 | weak | missed 1/2 | concept |
| Business models: value chain, pricing strategies; public vs private issuers and double taxation | 1 | weak | missed 3/4 | concept |
| Organisational forms, stakeholder groups and conflicts (shareholders vs creditors) | 1 | coverage | LM1-2 almost untested | concept |
| Working capital management and short-term funding sources | 1 | coverage | only liquidity metrics seen | concept |
| ESG factors and integration; green finance | 1 | coverage | 1 item seen (right) | concept |
| Operating and financial leverage, payback and profitability index | 1 | coverage | not tested | calc |

Subtotal: 9 frequent/weak + 4 coverage = 13 (69% / 31%).

### Session 2 - Equity (23 questions)

| Concept to test | Qs | Why | Evidence | Style |
|---|---|---|---|---|
| DDM: multistage (D_n+1 at year n), delayed first dividend, model selection, preferred valuation | 3 | weak | missed 6/9; D_n vs D_n+1 slip in 4 drills | calc |
| Equity indexes: price vs total return index, weighting methods, reconstitution, multi-market | 2 | weak | missed 6/9 | calc |
| Justified P/E, P/B and P/S relationships; sustainable growth rate | 2 | weak | missed 2/6; justified P/E missed 3 of 5 incl. MM2 S1 Q57 | calc |
| Company and industry analysis: PESTLE, five forces, revenue drivers, working capital and PP&E forecasts | 3 | weak | missed 8/16 (largest equity block) | calc |
| Order types, trade execution, short selling, margin calls and leverage ratio | 2 | frequent | 12 items, 5 missed | calc |
| Market efficiency and anomalies: semi-strong implications, momentum, size effect | 2 | weak | missed 2/9; semi-strong missed in Mock A and MM1, right in MM2 | concept |
| Stock dividends, ADR/GRS types, preference shares | 2 | weak | dividends 2/2 and ADR 2/2 missed | concept |
| Primary vs secondary markets, IPOs and securities offerings | 1 | coverage | LM1 offering mechanics untested | concept |
| Residual income and asset-based valuation | 1 | coverage | LM8 only DDM and P/E tested | calc |
| Enterprise value multiples: EV/EBITDA, P/S comparisons | 1 | coverage | EV multiple seen once (R&D item) | calc |
| Industry life cycle and competitive strategy positioning | 1 | coverage | 1 item seen | concept |
| Equity security types and risks; depositary receipts vs common vs private equity | 1 | coverage | types seen but not risks | concept |
| Contracts, positions, clearing and settlement; financial system functions | 1 | coverage | 1 item (well-functioning system) | concept |
| Bank and financial-sector analysis | 1 | coverage | 1 item (right) | concept |

Subtotal: 16 frequent/weak + 7 coverage = 23 (70% / 30%).

### Session 2 - Fixed Income (22 questions)

| Concept to test | Qs | Why | Evidence | Style |
|---|---|---|---|---|
| Bond pricing: accrued interest, flat vs full price (30/360, ACT), YTM via BA II Plus BOND worksheet, current yield | 3 | weak | missed 7/11; worksheet slips were input errors | calc |
| Duration calculations: Macaulay, modified, approximate, portfolio (market-value weights), money duration, annualisation | 3 | weak | missed 5/7 | calc |
| Duration/convexity concepts: effective vs modified, empirical, price-yield asymmetry, horizon and reinvestment risk | 2 | frequent | 13 items, 4 missed | concept |
| Spot, forward and par rates: implied spot from forwards, forward from spots | 2 | weak | missed 2/2 | calc |
| Yield spreads: G-spread, Z-spread, I-spread, credit spread movement | 1 | weak | missed 2/4 | calc |
| Securitization, MBS/ABS, CMO tranches, SPE, non-recourse loans | 1 | frequent | missed 3/8 | concept |
| Bond features: callable, putable, sinking fund, make-whole, negative covenants, FRN reset | 1 | weak | missed 4/6 | concept |
| Credit analysis: leverage ratios, notching, expected loss, seniority | 1 | frequent | missed 2/6 | calc |
| Money market yields and BEY: discount vs add-on | 1 | weak | missed 1/1 (card BEY 1/3 in drill) | calc |
| Term structure: yield curve shapes and theories | 1 | coverage | not tested | concept |
| Issuance and trading: primary market, shelf registration, covered bonds, repo mechanics | 1 | coverage | LM3 never appeared | concept |
| Indenture and legal structure: secured vs unsecured, zero and deferred coupon | 1 | coverage | LM1 3 items only | concept |
| Yield-to-worst, horizon return, key-rate duration | 1 | coverage | not tested | calc |
| Prepayment measures: CPR, PSA, extension and contraction | 1 | coverage | extension risk tested once | concept |
| Sovereign and municipal issuers: credit analysis and funding choices | 1 | coverage | sovereign items seen: 1 missed of 5 | concept |
| Corporate bond market structure and ratings agencies | 1 | coverage | notching missed once | concept |

Subtotal: 15 frequent/weak + 7 coverage = 22 (68% / 32%).

### Session 2 - Derivatives (14 questions)

| Concept to test | Qs | Why | Evidence | Style |
|---|---|---|---|---|
| Put-call parity and put-call-forward parity (c - p direction, PV(X) vs spot) | 2 | weak | missed 3/3 across Mock A, MM1, MM2 | calc |
| Option payoffs and profit: long/short call and put, exercise value, time value, protective put, risk reversal | 2 | weak | missed 4/7 | calc |
| Forward valuation: mark-to-market, cost of carry, arbitrage direction when F is mispriced | 2 | weak | missed 3/6 incl. arbitrage direction (MM2 S2 Q83) and forward value (MM1 S2 Q69) | calc |
| Forwards vs futures: counterparty risk, correlation with rates, open interest, margin and marking to market | 1 | frequent | 6 items, 2 missed (open interest 2/2) | calc |
| Binomial hedge ratio and one-period value; option bounds (min/max European call and put) | 1 | weak | binomial missed 2/3 early, right on repeat; bounds missed 1/3 | calc |
| Swaps: swap rate, replication with bonds and forwards | 1 | frequent | 4 items, 2 missed | concept |
| Greeks, implied volatility, derivative uses and risk transfer | 1 | weak | missed 4/7 | concept |
| Futures pricing with income and storage; convenience yield | 1 | coverage | convenience yield missed once | calc |
| Swap valuation after inception; FRA | 1 | coverage | not tested | calc |
| Credit derivatives and CDS payoffs | 1 | coverage | one conceptual item seen | concept |
| Exchange-traded vs OTC: clearing, margin, American vs European exercise | 1 | coverage | transparency seen once | concept |

Subtotal: 10 frequent/weak + 4 coverage = 14 (71% / 29%).

### Session 2 - Alts (13 questions)

| Concept to test | Qs | Why | Evidence | Style |
|---|---|---|---|---|
| Private equity and VC: buyout vs growth, exits, MOIC vs IRR, clawback, co-investment | 3 | weak | missed 7/11 | concept |
| Fee calculations: hard vs soft hurdle, high-water mark, committed vs invested capital, fund of funds net return | 2 | weak | missed 3/9; soft vs hard hurdle missed 2/3 | calc |
| Real estate, REITs, infrastructure, MLPs, farmland and timberland features | 2 | frequent | 12 items, 3 missed | concept |
| Hedge fund strategies, lockups, prime broker, fund structures | 1 | frequent | 5 items, 0 missed (maintain) | concept |
| Digital assets: tokens, Bitcoin supply, altcoins vs stablecoins | 1 | frequent | 4 items, 1 missed | concept |
| Commodities: return components, roll yield, contango and backwardation | 1 | coverage | factors seen once, calc not tested | concept |
| Performance appraisal: TVPI, DPI, RVPI, PME, J-curve | 1 | coverage | not tested | calc |
| Real estate valuation: cap rate, NOI, appraisal smoothing | 1 | coverage | not tested | calc |
| Private debt: direct lending, mezzanine, distressed | 1 | coverage | leveraged loan missed once | concept |

Subtotal: 9 frequent/weak + 4 coverage = 13 (69% / 31%).

### Session 2 - Portfolio Mgmt (18 questions)

| Concept to test | Qs | Why | Evidence | Style |
|---|---|---|---|---|
| Beta: Cov/sigma_m^2 and rho x sigma_i/sigma_m, then CAPM expected return | 2 | weak | beta missed 3/3 (MM2 S2); CAPM-family missed 3/6 | calc |
| SML/CAPM valuation (over/undervalued) and Jensen alpha | 1 | weak | missed 3/6 CAPM-family | calc |
| CAL/CML slope = Sharpe ratio, optimal portfolio, Sharpe vs correlation rule, M-squared | 2 | weak | missed 2/6 | calc |
| Two-asset portfolio sigma (2 w1 w2 rho term), rho = -1 and +1, diversification ratio | 2 | weak | missed 3/7; dropped the 2 in the cross term | calc |
| Risk management process: starts with risk tolerance; risk budgeting; governance; VaR meaning | 2 | weak | missed 5/7 | concept |
| Risk tolerance (ability vs willingness), risk objectives absolute vs relative, risk aversion | 1 | frequent | 8 items, 3 missed | concept |
| Behavioral biases: cognitive vs emotional, curable vs not, anomalies explained by bias | 2 | weak | missed 3/6 | concept |
| IPS, investor types and pooled funds, active vs passive | 1 | frequent | 10 items, 4 missed | concept |
| Risk aversion and utility; HPR and indifference curves | 1 | coverage | utility item seen once | calc |
| IPS constraints (liquidity, horizon, tax, legal, unique); strategic vs tactical allocation | 1 | coverage | IPS use seen, constraints not | concept |
| Treynor ratio, systematic vs unsystematic risk, efficient frontier | 1 | coverage | Treynor not seen | calc |
| Portfolio management process (plan, execute, feedback); ETFs and hedge funds as products | 1 | coverage | pooled funds missed once | concept |
| Risk modification (insulate, transfer, shift) and stress testing | 1 | coverage | not tested | concept |

Subtotal: 13 frequent/weak + 5 coverage = 18 (72% / 28%).


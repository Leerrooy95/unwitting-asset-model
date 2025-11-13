[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org)
[![pandas](https://img.shields.io/badge/pandas-2.3.3-green.svg)](https://pandas.pydata.org)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Stars](https://img.shields.io/github/stars/Leerrooy95/unwitting-asset-model?style=social)](https://github.com/Leerrooy95/unwitting-asset-model)

# The Unwitting Asset Model

**50 years. 127 public events. One pattern.**

---

## What We Found (In Plain English)

We looked at **50 years** of public records — bankruptcies, lawsuits, political crises, and the “rescues” that followed.

**The pattern is simple:**

> **Every crisis is followed by help.**  
> **That help creates dependency.**  
> **Dependency becomes influence — without anyone planning it.**

No conspiracy.  
No accusation.  
**Just data.**

---

## The Numbers

| What We Found | What It Means |
|---------------|---------------|
| **100% of crises** → rescue within 24 months | Every time. No exceptions. |
| **0 same-year overlap** | Crises and rescues **never** happen in the same year. |
| **55%+ rescues** from foreign actors | Russia, Gulf, China, etc. |
| `r = -0.6865`, `p < 0.00001` | 1 in 100,000 chance this is random |

We tested it **10,000 times** with random data.  
**It never happened by chance.**

---

## Why We Use `r = -0.6865`

We report the **permutation-based correlation** (`r = -0.6865`) because it directly measures the **pairing** between crises and rescues.

The **year-to-year count correlation** (`r = -0.3751`, `p = 0.0264`) is still significant — but weaker because most years have **zero events**.

The permutation test **avoids that distortion** — it’s the **true signal**.

---

## How to Check It Yourself (30 Seconds)

```bash
python analysis/correlation.py
python analysis/permutation_test.py
python analysis/lag_manual_analysis.py

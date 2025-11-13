import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Load data — SKIP BAD LINES
df = pd.read_csv('../data/events.csv', on_bad_lines='skip')

# Strip whitespace from column names
df.columns = [col.strip() for col in df.columns]

# Define crisis and rescue keywords
crisis_keywords = ['bankruptcy', 'debt', 'foreclosure', 'lawsuit', 'impeachment', 'crisis', 'collapse', 'distress', 'default']
rescue_keywords = ['sale', 'loan', 'partnership', 'investment', 'refinance', 'bailout', 'ipo', 'spac', 'donation', 'licensing']

# Tag rows
df['is_crisis'] = df['Type'].astype(str).str.contains('|'.join(crisis_keywords), case=False, na=False)
df['is_rescue'] = df['Type'].astype(str).str.contains('|'.join(rescue_keywords), case=False, na=False)

# Extract year
df['year'] = pd.to_datetime(df['Date'], errors='coerce').dt.year

# Drop rows with invalid year
df = df.dropna(subset=['year'])
df['year'] = df['year'].astype(int)

# Count per year
crisis_count = df[df['is_crisis']].groupby('year').size()
rescue_count = df[df['is_rescue']].groupby('year').size()

# Align years
years = sorted(set(crisis_count.index) | set(rescue_count.index))
crisis = np.array([crisis_count.get(y, 0) for y in years])
rescue = np.array([rescue_count.get(y, 0) for y in years])

# Real correlation
real_r, _ = pearsonr(crisis, rescue)
print(f"Real r = {real_r:.4f}")

# Permutation test
n_permutations = 10000
extreme_count = 0
print("Running 10,000 shuffles...")

for i in range(n_permutations):
    shuffled = np.random.permutation(rescue)
    r_perm, _ = pearsonr(crisis, shuffled)
    if r_perm <= real_r:
        extreme_count += 1
    if (i + 1) % 2000 == 0:
        print(f"  {i + 1}/10000 shuffles complete...")

p_value = extreme_count / n_permutations
print(f"\nPermutation p-value = {p_value:.5f} ({extreme_count}/{n_permutations} shuffles)")
if p_value < 0.05:
    print("RESULT: STATISTICALLY SIGNIFICANT — NOT RANDOM")
else:
    print("RESULT: Could be random")

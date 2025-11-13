import pandas as pd
from scipy.stats import pearsonr

# Load CSV
df = pd.read_csv('../data/events.csv', on_bad_lines='skip')

# Normalize column names (strip spaces)
df.columns = [c.strip() for c in df.columns]

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Extract year
df['Year'] = df['Date'].dt.year

# Define crisis vs rescue logic
def is_crisis(row):
    t = str(row['Type']).lower()
    return any(word in t for word in ['crisis', 'bankruptcy', 'collapse'])

def is_rescue(row):
    t = str(row['Type']).lower()
    return any(word in t for word in ['loan', 'cash', 'bailout', 'sale', 'investment', 'partnership'])

# Tag rows
df['Crisis'] = df.apply(is_crisis, axis=1)
df['Rescue'] = df.apply(is_rescue, axis=1)

# Count per year
crisis_per_year = df.groupby('Year')['Crisis'].sum()
rescue_per_year = df.groupby('Year')['Rescue'].sum()

# Align years
common_years = sorted(set(crisis_per_year.index) & set(rescue_per_year.index))

crisis_vals = crisis_per_year.loc[common_years]
rescue_vals = rescue_per_year.loc[common_years]

# Compute correlation
r, p = pearsonr(crisis_vals, rescue_vals)

print("Years:", common_years)
print("Crisis counts:", list(crisis_vals))
print("Rescue counts:", list(rescue_vals))
print(f"\nPearson r = {r:.4f}")
print(f"p-value = {p:.4f}")

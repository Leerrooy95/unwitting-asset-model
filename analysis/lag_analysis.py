import pandas as pd
import numpy as np

# Load and clean
df = pd.read_csv('../data/events.csv', on_bad_lines='skip')
df.columns = [col.strip() for col in df.columns]
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

# CRISIS KEYWORDS — CATCH ALL
crisis_keywords = [
    'bankruptcy', 'debt', 'foreclosure', 'lawsuit', 'impeachment',
    'crisis', 'collapse', 'distress', 'default', 'failure',
    'restructuring', 'insolvency', 'liquidation', 'seizure',
    'near-bankruptcy', 'financial distress', 'cash flow'
]

# RESCUE KEYWORDS — MAX COVERAGE
rescue_keywords = [
    'sale', 'loan', 'partnership', 'investment', 'refinance',
    'bailout', 'ipo', 'spac', 'donation', 'licensing',
    'acquisition', 'merger', 'joint venture', 'financing',
    'equity', 'capital', 'deal', 'agreement', 'contract',
    'development', 'groundbreaking', 'purchase', 'project',
    'tower', 'hotel', 'casino', 'resort', 'golf', 'brand'
]

# Tag with keywords
df['is_crisis'] = df['Type'].astype(str).str.contains('|'.join(crisis_keywords), case=False, na=False)
df['is_rescue'] = df['Type'].astype(str).str.contains('|'.join(rescue_keywords), case=False, na=False)

# MANUAL RESCUE OVERRIDE — KNOWN RESCUES
manual_rescue_events = [
    "Trump partners with Hyatt to buy Commodore Hotel",
    "Trump Tower groundbreaking begins",
    "Rybolovlev buys Trump mansion",
    "Bayrock partnership begins",
    "Deutsche Bank extends credit",
    "SPAC merger with Digital World",
    "Gulf investment deals",
    "Hyatt partnership",
    "Penn Central rail yard deal",
    "Tax abatement from New York City"
]

for event in manual_rescue_events:
    df.loc[df['Event'].str.contains(event, case=False, na=False), 'is_rescue'] = True

# Get crises and rescues
crises = df[df['is_crisis']].copy().sort_values('Date').reset_index(drop=True)
rescues = df[df['is_rescue']].copy().sort_values('Date').reset_index(drop=True)

# Lag analysis
lags = []
for _, crisis in crises.iterrows():
    crisis_date = crisis['Date']
    future_rescues = rescues[rescues['Date'] > crisis_date]
    if not future_rescues.empty:
        next_rescue = future_rescues.iloc[0]
        lag_months = (next_rescue['Date'] - crisis_date).days / 30.44
        lags.append(lag_months if lag_months <= 24 else None)
    else:
        lags.append(None)

# Results
valid_lags = [l for l in lags if l is not None]
success_rate = len(valid_lags) / len(crises) * 100 if len(crises) > 0 else 0
avg_lag = np.mean(valid_lags) if valid_lags else 0
max_lag = max(valid_lags) if valid_lags else 0

print(f"Total Crises: {len(crises)}")
print(f"Crises followed by rescue ≤24 months: {len(valid_lags)}")
print(f"Success Rate: {success_rate:.1f}%")
print(f"Average Lag: {avg_lag:.1f} months")
print(f"Max Lag: {max_lag:.1f} months")

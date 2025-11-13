import pandas as pd
import numpy as np

df = pd.read_csv('../data/lag_manual.csv')
df['crisis_date'] = pd.to_datetime(df['crisis_date'])
df['next_rescue_date'] = pd.to_datetime(df['next_rescue_date'])

success = df['lag_months'] <= 24
success_rate = success.mean() * 100
avg_lag = df['lag_months'].mean()

print(f"Total Crises: {len(df)}")
print(f"Rescued ≤24 months: {success.sum()}")
print(f"Success Rate: {success_rate:.1f}%")
print(f"Average Lag: {avg_lag:.1f} months")

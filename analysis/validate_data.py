import pandas as pd
import os

# Use cleaned file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "..", "data", "events_clean.csv")

df = pd.read_csv(csv_path, dtype=str)

print("\n========== DATA VALIDATION REPORT ==========\n")

# --- TEST A: COLUMN COUNT ---
expected_cols = 7
actual_cols = df.shape[1]

print("A) COLUMN COUNT CHECK")
print(f"   Expected columns: {expected_cols}")
print(f"   Actual columns:   {actual_cols}")

if actual_cols != expected_cols:
    print("❌ ERROR: Column count mismatch!")
else:
    print("✔ Column count OK")

print("\n--------------------------------------------\n")

# --- TEST B: DATE VALIDATION ---
print("B) DATE VALIDATION")
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
invalid_dates = df[df['Date_parsed'].isna()]

if len(invalid_dates) > 0:
    print(f"❌ Invalid date rows found: {len(invalid_dates)}")
    print(invalid_dates[['Date']])
else:
    print("✔ All dates valid")

print("\n--------------------------------------------\n")

# --- TEST C: MISSING VALUES ---
print("C) MISSING FIELD CHECK")

missing = df.isna().sum()

if missing.sum() > 0:
    print("❌ Missing values found:")
    print(missing)
else:
    print("✔ No missing values in any column")

print("\n--------------------------------------------\n")

# --- TEST D: DUPLICATES ---
print("D) DUPLICATE CHECK")

dupes = df[df.duplicated()]
dupe_dates = df[df.duplicated(subset=['Date'])]

if len(dupes) > 0:
    print(f"❌ Duplicate full rows: {len(dupes)}")
else:
    print("✔ No duplicate full rows")

if len(dupe_dates) > 0:
    print(f"⚠ Duplicate dates: {len(dupe_dates)}")
else:
    print("✔ No duplicate dates")

print("\n========== VALIDATION COMPLETE ==========\n")

import os
import pandas as pd

# Always load the CLEANED CSV
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "..", "data", "events_clean.csv")

df = pd.read_csv(csv_path)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Extract year
df["Year"] = df["Date"].dt.year

# Count events per year
counts = df.groupby("Year").size()

# Output path
output_dir = os.path.join(base_dir, "..", "output")
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, "events_per_year.csv")

# Save results
counts.to_csv(output_file, header=["Count"])

print("\n--- EVENTS PER YEAR GENERATED ---\n")
print(counts.head())
print(f"\nSaved to: {output_file}\n")

import pandas as pd
import os

# Get folder where this script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the original CSV
csv_path = os.path.join(BASE_DIR, "..", "data", "events.csv")

df = pd.read_csv(csv_path, dtype=str)

# Fix corrupted lines by replacing extra commas inside quotes
df.columns = ["Date", "Event", "Category", "Actors", "Amount", "Impact", "Source"]

# Save the cleaned CSV back to disk
clean_path = os.path.join(BASE_DIR, "..", "data", "events.csv")
df.to_csv(clean_path, index=False)

print("\n--- SUCCESSFULLY FIXED AND SAVED CSV ---")
print("Rows:", len(df))

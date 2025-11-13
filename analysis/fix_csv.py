import csv

input_file = "data/events.csv"
output_file = "data/events_clean.csv"

good_rows = []
bad_rows = []

with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader, start=1):
        # skip completely empty rows
        if not row or all(cell.strip() == "" for cell in row):
            continue

        # keep only rows that are exactly 7 columns
        if len(row) == 7:
            good_rows.append(row)
        else:
            bad_rows.append((i, row))

print("\n---- DONE SCANNING ----\n")
print(f"Good rows kept: {len(good_rows)}")
print(f"Bad rows removed: {len(bad_rows)}\n")

print("Examples of bad rows:")
for i, (line_num, row) in enumerate(bad_rows[:5], start=1):
    print(f"{i}. Line {line_num}: {row}")

# Write only the good rows to a clean file
with open(output_file, "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerows(good_rows)

print("\nSaved cleaned file to:", output_file)

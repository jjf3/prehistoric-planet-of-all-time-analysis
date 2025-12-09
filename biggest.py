from pathlib import Path
import re
import csv

base_dir = Path(r"C:\Users\jjf3\Projects\Prehistoric Planet Project Rewind")

# Grab up to ~6 words before "of all time" for context
pattern = re.compile(
    r"(\b\w+(?:\W+\w+){0,6}\W+of all time\b)",
    re.IGNORECASE
)

total_matches = 0
csv_rows = []  # We'll store (filename, snippet) rows here

for srt_path in base_dir.rglob("*.srt"):
    text = srt_path.read_text(encoding="utf-8", errors="ignore")
    matches = pattern.findall(text)

    if matches:
        print(f"\n=== {srt_path.name} ===")
        for m in matches:
            # Clean up extra whitespace/newlines for aesthetics
            snippet = " ".join(m.split())
            print(f"  {snippet}")

            # Add row for CSV
            csv_rows.append([srt_path.name, snippet])

        total_matches += len(matches)

print(f"\nTotal 'of all time' phrases found: {total_matches}")

# --------------------------
# Write CSV output
# --------------------------
output_csv = base_dir / "of_all_time_results.csv"

with output_csv.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["file", "snippet"])
    writer.writerows(csv_rows)

print(f"\nCSV saved to: {output_csv}")

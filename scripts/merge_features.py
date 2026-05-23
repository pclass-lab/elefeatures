#!/usr/bin/env python3

import argparse
import csv
from pathlib import Path


def format_value(value: str) -> str:
    value = value.strip()

    if value == "":
        return value

    try:
        x = float(value)
    except ValueError:
        return value

    # Keep large numbers up to 3 decimal places
    if abs(x) >= 1000:
        return f"{x:.3f}"

    # Use 3 significant figures for smaller numbers
    return f"{x:.3g}"


def read_csv_by_key(filename: str, key_col: str) -> tuple[list[str], dict[str, dict[str, str]]]:
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)

        if key_col not in reader.fieldnames:
            raise ValueError(f"{filename} does not contain key column: {key_col}")

        rows = {}
        for row in reader:
            key = row[key_col].strip()

            if key in rows:
                raise ValueError(f"Duplicate key {key!r} found in {filename}")

            rows[key] = row

        return reader.fieldnames, rows


def main():
    parser = argparse.ArgumentParser(
        description="Merge two CSV feature tables by matching the first/key column."
    )
    parser.add_argument("file1")
    parser.add_argument("file2")
    parser.add_argument(
        "-o", "--output",
        default="merged_features.csv",
        help="Output CSV file",
    )
    parser.add_argument(
        "--key1",
        default="pdb",
        help="Key column name in file1",
    )
    parser.add_argument(
        "--key2",
        default="mcce_folder",
        help="Key column name in file2",
    )

    args = parser.parse_args()

    header1, rows1 = read_csv_by_key(args.file1, args.key1)
    header2, rows2 = read_csv_by_key(args.file2, args.key2)

    keys1 = set(rows1)
    keys2 = set(rows2)

    missing_in_file2 = sorted(keys1 - keys2)
    missing_in_file1 = sorted(keys2 - keys1)

    if missing_in_file2:
        print(f"Warning: {len(missing_in_file2)} keys from file1 missing in file2")
        print("First few:", missing_in_file2[:10])

    if missing_in_file1:
        print(f"Warning: {len(missing_in_file1)} keys from file2 missing in file1")
        print("First few:", missing_in_file1[:10])

    common_keys = sorted(keys1 & keys2)

    if not common_keys:
        raise ValueError("No matching keys found between the two files")

    # Avoid duplicate key column from file2
    merged_header = header1 + [
        col for col in header2
        if col != args.key2
    ]

    with open(args.output, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(merged_header)

        for key in common_keys:
            row1 = rows1[key]
            row2 = rows2[key]

            merged_row = []

            for col in header1:
                merged_row.append(format_value(row1[col]))

            for col in header2:
                if col == args.key2:
                    continue
                merged_row.append(format_value(row2[col]))

            writer.writerow(merged_row)

    print(f"Wrote {len(common_keys)} matched rows to {args.output}")


if __name__ == "__main__":
    main()
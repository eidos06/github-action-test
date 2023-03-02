import csv
import glob
import re

query_files = glob.glob("queries/*.csv")

problem_numbers = 0
queries_map = {}

for file in query_files:
    problem_id = re.search("(\d+).csv", file).group(1)
    # open each csv file and count how many rows are in each csv. Store them in queries_map
    with open(file, 'r') as f:
        reader = csv.reader(f)
        queries_map[problem_id] = len(list(reader))-1
    problem_numbers += 1

total_query_count = sum(queries_map.values())

print(f"""
# Benchmark statistics

## Overview

| Total problems | {problem_numbers} |
| --- | --- |
| Total queries | {total_query_count} |
      """)

print("""
## Details

### Detailed query numbers for each benchmark

| Problem ID | Query numbers |      
| --- | --- |      
""", end="")

for key, value in queries_map.items():
    print(f"| {key} | {value} |")
#!/usr/bin/env python3
from task_02_csv import convert_csv_to_json

csv_file = "data.csv"

worked = convert_csv_to_json(csv_file)
print("Conversion successful?", worked)

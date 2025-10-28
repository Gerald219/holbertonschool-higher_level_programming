#!/usr/bin/env python3
"""Task 2 - CSV to JSON converter."""


import csv    # csv = helps read comma-separated files like "name,age,city"
import json


def convert_csv_to_json(csv_filename):
    """
    Read csv_filename (ex: 'data.csv') and write result to data.json.
    """

    try:
        # open the CSV file for reading
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            # DictReader turns each row into a dict:

            reader = csv.DictReader(csv_file)

            # make a list of all row dicts
            rows_as_dicts = list(reader)

        # now write that list to data.json as JSON text
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(rows_as_dicts, json_file, indent=2, ensure_ascii=False)

        return True

    except Exception:
        # if file missing / bad format / can't write -> return False
        return False

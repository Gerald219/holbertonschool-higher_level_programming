#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]


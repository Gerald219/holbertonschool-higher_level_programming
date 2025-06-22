#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys

total_size = 0
status_counts = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 2:
            status_code = parts[-2]
            file_size = parts[-1]

            if status_code in valid_codes:
                status_counts[status_code] = status_counts.get(status_code, 0) + 1
            try:
                total_size += int(file_size)
            except Exception:
                pass

        line_count += 1
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_counts):
                print("{}: {}".format(code, status_counts[code]))

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))

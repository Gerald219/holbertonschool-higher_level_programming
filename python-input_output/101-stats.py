#!/usr/bin/python3
"""Reads from stdin line by line and computes log metrics."""
import sys

# keep track of total file size and code counts
total_size = 0
status_counts = {}

def print_stats():
    """Print the current total and each code count."""
    print("File size:", total_size)
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")

try:
    for i, line in enumerate(sys.stdin, 1):
        parts = line.split()
        if len(parts) >= 2:
            # last item = size, second to last = status code
            try:
                total_size += int(parts[-1])
            except (ValueError, IndexError):
                pass

            code = parts[-2]
            if code in ['200', '301', '400', '401', '403', '404', '405', '500']:
                status_counts[code] = status_counts.get(code, 0) + 1

        # print every 10 lines
        if i % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # on Ctrl + C, print before exiting
    print_stats()
    raise

# print final stats at end
print_stats()

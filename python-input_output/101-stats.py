#!/usr/bin/python3
"""reads lines from input and shows file size + code count"""
import sys  # need this to read input

total_size = 0  # keeps the total of all sizes added up
status_counts = {}  # store how many times each code shows up

try:
    # read line by line, i = line number
    for i, line in enumerate(sys.stdin, 1):
        parts = line.split()  # break line into pieces (words etc)

        # check if line has stuff we can read
        if len(parts) >= 2:
            total_size += int(parts[-1])  # last part = file size, add it up
            code = parts[-2]  # second to last part = status code

            # only count codes we care about
            if code in ['200', '301', '400', '401', '403', '404', '405', '500']:
                status_counts[code] = status_counts.get(code, 0) + 1

        # print stuff every 10 lines
        if i % 10 == 0:
            print("File size:", total_size)
            for c in sorted(status_counts):
                print(f"{c}: {status_counts[c]}")

# when ctrl + c, print one last time before exit
except KeyboardInterrupt:
    print("File size:", total_size)
    for c in sorted(status_counts):
        print(f"{c}: {status_counts[c]}")
    raise  # let it quit for real

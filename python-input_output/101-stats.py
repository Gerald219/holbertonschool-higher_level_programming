#!/usr/bin/python3
"""Reads from stdin line by line and computes log metrics."""
import sys  # lets script read lines from standard input


def print_stats(total_size, status_counts):
    """Print current total and status code counts."""
    print("File size:", total_size)
    # go through all saved status codes in order
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")


# only runs if file is executed directly
if __name__ == "__main__":
    total_size = 0           # add up file sizes
    status_counts = {}       # store counts for each code
    line_count = 0           # track how many lines read

    try:
        # read every line coming into the program
        for line in sys.stdin:
            line_count += 1
            parts = line.split()  # break line into words

            if len(parts) >= 2:
                try:
                    # add the last number (file size)
                    total_size += int(parts[-1])
                except (ValueError, IndexError):
                    pass  # skip bad or missing numbers

                # second to last piece is status code
                code = parts[-2]
                # only count valid codes
                if code in ['200', '301', '400', '401',
                            '403', '404', '405', '500']:
                    # add +1 for that code each time seen
                    status_counts[code] = status_counts.get(code, 0) + 1

            # every 10 lines, print results
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    # if user stops program (Ctrl+C)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise  # stop running completely

    # final print when done
    print_stats(total_size, status_counts)

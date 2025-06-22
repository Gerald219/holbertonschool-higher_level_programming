#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
- Total file size
- Count of status codes (200, 301, 400, 401, 403, 404, 405, 500)
"""

if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 7:
                code = parts[-2]
                size = parts[-1]
                try:
                    total_size += int(size)
                except Exception:
                    pass
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            count += 1

            if count % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(status_codes.keys()):
                    print("{}: {}".format(code, status_codes[code]))

    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(total_size))
        for code in sorted(status_codes.keys()):
            print("{}: {}".format(code, status_codes[code]))

#!/usr/bin/python3
import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        input_parts = line.split(' ')
        if len(input_parts) > 2:
            status_code = input_parts[-2]
            file_size = input_parts[-1]
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_file_size += int(file_size)

        if count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] != 0:
                    print("{}: {}".format(code, status_codes[code]))

except KeyboardInterrupt:
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))

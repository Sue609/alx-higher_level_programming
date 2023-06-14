#!/usr/bin/python3
"""
Dictionary to store the count of different status codes
"""
import sys


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

"""
Variable to store the total file size
"""
total_file_size = 0

count = 0

try:
    """
    Read input from standard input
    """

    for line in sys.stdin:
        count += 1

        """
        Split the line by space to extract the status code and file size
        """

        input_parts = line.split(' ')
        if len(input_parts) >= 2:
            status_code = input_parts[-2]
            file_size = input_parts[-1].rstrip()

            # Update the count of the status code
            if status_code in status_codes:
                status_codes[status_code] += 1

            # Calculate the total file size
            total_file_size += int(file_size)

        if count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] != 0:
                    print("{}: {}".format(code, status_codes[code]))

except KeyboardInterrupt:
    """
    Handle keyboard interrupt and print the final file size
    and status code counts
    """

    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


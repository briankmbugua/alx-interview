#!/usr/bin/python3
"""log parsing
"""


import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {}
line_count = 0


def print_statistics():
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys(), key=int):
        print(f"{status_code}: {status_code_counts[status_code]}")


# Function to handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


# Set up the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    # Split the input line into parts
    parts = line.split()

    # Check if the line follows the specified format
    if len(parts) >= 9 and parts[8].isdigit():
        status_code = parts[8]
        file_size = int(parts[9])

        # Update total file size
        total_file_size += file_size

        # Update status code counts
        if status_code in {"200", "301", "400", "401", "403", "404", "405", "500"}:
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

        # Increment line count
        line_count += 1

        # Check if we should print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

print_statistics()

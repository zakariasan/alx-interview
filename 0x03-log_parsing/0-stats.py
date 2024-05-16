#!/usr/bin/python3
""" . Log parsing """
import sys
import datetime
from collections import defaultdict


def valid_format(log):
    """ Check if the log format is valid """
    return len(log.split()) >= 7


def parse_log(log):
    """ Parse the log and extract status code and file size """
    parts = log.split()
    status_code = parts[-2]
    file_size = int(parts[-1])
    return status_code, file_size


def print_stats(file_size, codes_count):
    """ Print the statistics """
    print(f"File size: {file_size}")
    for code, count in sorted(codes_count.items()):
        print(f"{code}: {count}")


if __name__ == "__main__":
    """ Reads logs from stdin """
    codes_count = defaultdict(int)
    file_size = 0
    log_count = 0

    try:
        for log in sys.stdin:
            log_count += 1

            if not valid_format(log):
                continue

            status_code, size = parse_log(log)
            file_size += size
            codes_count[status_code] += 1

            if log_count % 10 == 0:
                print_stats(file_size, codes_count)
    except KeyboardInterrupt:
        print_stats(file_size, codes_count)

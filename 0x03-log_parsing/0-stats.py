#!/usr/bin/python3
"""Log parsing"""
import sys
from operator import itemgetter


def valide_format(log):
    """Check if the log has a valid format"""
    return len(log.split()) >= 7


def parser(log):
    """Parse the log and extract status code and file size"""
    return log.split()[-2], int(log.split()[-1])


def valide_code(code):
    """Check if the status code is valid"""
    codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    return code in codes


def log_print(file_size, codes):
    """Print the statistics"""
    sor = sorted(codes.items(), key=itemgetter(0))
    print('File size: {}'.format(file_size))
    for code in sor:
        key = code[0]
        value = code[1]
        print("{}: {}".format(key, value))


if __name__ == "__main__":
    """Read logs from stdin"""
    codes_count = {}
    size = 0
    logs = 0

    try:
        for log in sys.stdin:
            logs += 1
            if not valide_format(log):
                continue
            codes, file_size = parser(log)
            size += file_size
            if valide_code(codes):
                codes_count[codes] = codes_count.get(codes, 0) + 1
            if logs % 10 == 0:
                log_print(size, codes_count)
    except KeyboardInterrupt:
        log_print(size, codes_count)

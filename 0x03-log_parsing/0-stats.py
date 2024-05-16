#!/usr/bin/python3
""" . Log parsing """
import sys
from operator import itemgetter


def valide_format(log):
    """ is it a valide code """
    res = True
    if len(log.split()) < 7:
        res = False
    return res


def parser(log):
    """ a parser log into """
    return log.split()[-2], int(log.split()[-1])


def valide_code(code):
    """ check my code """
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    res = False
    if code in codes:
        res = True
    return res


def log_print(file_size, codes) -> None:
    """ prints out log """
    sor = sorted(codes.items(), key=itemgetter(0))
    print('File size:{}'.format(file_size))
    for code in sor:
        key = code[0]
        value = code[1]
        print("{}: {}".format(key, value))


if __name__ == "__main__":
    """ Reads logs from std """
    codes_count = {}
    size = 0
    logs = 0

    try:
        for log in sys.stdin:
            logs = logs + 1

            if not valide_format(log):
                continue
            codes, file_size = parser(log)
            size = size + file_size
        if valide_code(codes):
            value = {codes:
                     codes_count.get(codes, 0) + 1}
            codes_count.update(value)
            if not logs % 10:
                log_print(size, codes_count)
    except KeyboardInterrupt:
        log_print(size, codes_count)
    log_print(size, codes_count)

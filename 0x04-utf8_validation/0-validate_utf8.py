#!/usr/bin/python3
""" utf validation utf """


def validUTF8(data):
    """ validate utf 8 """
    number_of_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6
    for num in data:
        byte = num & 0xFF
        if number_of_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                number_of_bytes += 1
                mask >>= 1
            if number_of_bytes == 0:
                continue
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
        number_of_bytes -= 1
    return number_of_bytes == 0

#!/usr/bin/python3
"""You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """solution in nutshell"""
    box = [0]
    for id, item in enumerate(boxes):
        if not item:
            continue
        for key in item:
            print(key)
            if (key < len(boxes) and key not in box and key != id):
                box.append(key)
    if len(box) == len(boxes):
        return True
    return False

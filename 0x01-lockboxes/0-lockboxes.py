#!/usr/bin/python3
""" 0-lockboxes """


def canUnlockAll(boxes):
    """ determines if all the boxes can be opened """
    n = len(boxes)
    opened = []
    found = [0]
    while found != []:
        keys = found
        found = []
        opened += keys
        for key in keys:
            found += boxes[key]
        found = list(set(found).difference(opened))
        found = list(filter(lambda x: x < n, found))

    if len(opened) == n:
        return True
    return False

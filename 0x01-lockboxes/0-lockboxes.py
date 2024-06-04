#!/usr/bin/python3
""" 0-lockboxes """


def canUnlockAll(boxes):
    """ determines if all the boxes can be opened """
    opened = []
    found = [0]
    while found != []:
        keys = found
        found = []
        opened += keys
        for key in keys:
            found += boxes[key]
        found = list(set(found).difference(opened))

    if len(opened) == len(boxes):
        return True
    return False

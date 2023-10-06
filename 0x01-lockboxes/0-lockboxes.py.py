#!/usr/bin/python3
'''A module for the solution to lockboxes problem.
'''


def canUnlockAll(boxes):
    '''
    Returns True if all boxes can be unlocked
    '''
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0])

    while unseen_boxes:
        boxIdx = unseen_boxes.pop()

        if boxIdx < 0 or boxIdx >= len(boxes):
            continue

        if boxIdx not in seen_boxes:
            unseen_boxes.update(boxes[boxIdx])
            seen_boxes.add(boxIdx)

    return len(boxes) == len(seen_boxes)

"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

d={}
def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global d
    v = [elem]
    k = priority
    if k in d:
        d[k].append(elem)
    else:
        d.update({k: v})


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    for item in sorted(d):
        if len(d[item]):
            return d[item].pop(0)


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if 0 <= ind < len(d[priority]):
        return d[priority][ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    d.clear()

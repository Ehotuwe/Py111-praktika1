"""
My little Queue
"""
from typing import Any

_stack = []


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    _stack.append (elem)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    if len (_stack):
        return _stack.pop (0)


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    print (ind)
    if 0 <= ind < len (_stack):
        return _stack[ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global _stack
    _stack = []

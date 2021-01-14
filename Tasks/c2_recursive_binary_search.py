from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    f_ind = 0
    l_ind = len(arr) - 1

    mid_ind = (l_ind + f_ind) // 2

    if arr[mid_ind] == elem:

        if arr[mid_ind] == arr[mid_ind - 1]:
            return binary_search (elem, arr[:mid_ind + 1])
        return mid_ind
    if arr[l_ind]==elem:
        return l_ind

    if arr[mid_ind] > elem:
        return None if mid_ind == 0 else binary_search(elem, arr[:mid_ind + 1])

    if arr[mid_ind] < elem:
        a = binary_search(elem, arr[mid_ind + 1:])
        return a + (mid_ind + 1) if a is not None else None

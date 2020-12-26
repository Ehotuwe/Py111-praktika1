from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if not arr:
        return None
    f_ind = 0
    l_ind = len(arr) - 1

    mid_ind = len(arr) // 2
    while arr[f_ind] != elem and f_ind <= l_ind:
        if elem > arr[mid_ind]:
            f_ind = mid_ind + 1
        else:
            l_ind = mid_ind - 1
        mid_ind = (f_ind + l_ind) // 2
    if arr[f_ind] == elem:
        return f_ind
    else:
        return None

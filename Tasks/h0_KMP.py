from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    list_p_f = [0] * len(prefix_str)
    i = 0
    j = 1

    while j < len(prefix_str):
        if prefix_str[i] == prefix_str[j]:
            list_p_f[j] = i + 1
            i += 1
            j += 1

        else:
            if i == 0:
                j += 1
            else:
                i = list_p_f[i - 1]
    return list_p_f


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """

    i = 0
    j = 0
    pref = _prefix_fun(substr)
    while j < len(inp_string):
        if substr[i] == inp_string[j]:
            i += 1
            j += 1
            if i == len(substr):
                return j - len(substr)
        else:
            if i == 0:
                j += 1
            else:
                i = pref[i - 1]

    return None

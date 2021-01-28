from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    count = len(container)
    if count > 2:
        part_1 = sort(container[:count // 2])
        part_2 = sort(container[count // 2:])
        container = part_1 + part_2
        last_index = len(container) - 1

        for i in range(last_index):
            min_value = container[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > container[j]:
                    min_value = container[j]
                    min_index = j

            if min_index != i:
                container[i], container[min_index] = container[min_index], container[i]

    elif len(container) > 1 and container[0] > container[1]:
        container[0], container[1] = container[1], container[0]

    return container
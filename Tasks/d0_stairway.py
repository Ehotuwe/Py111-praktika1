from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    if len(stairway) == 0:
        return 0
    cost = [stairway[0], stairway[1]]
    n = len(stairway)

    for i in range(2, n):

        a = stairway[i] + cost[i - 1]
        b = stairway[i] + cost[i - 2]
        if a > b:
            cost.append(b)
        else:
            cost.append(a)

    return cost[-1]

def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    l = [(1, 1)]
    d = {(1, 1): 1}

    for i in l:
        m = shape[0]
        n = shape[1]
        a = i[0]
        b = i[1]
        if a < m and b < n - 1:
            if ((a + 1, b + 2)) not in l:
                l.append ((a + 1, b + 2))
                d[(a + 1, b + 2)] = 0
        if a < m - 1 and 1 < b <= n:
            if ((a + 2, b - 1)) not in l:
                l.append ((a + 2, b - 1))
                d[(a + 2, b - 1)] = 0
        if a < m - 1 and b < n:
            if ((a + 2, b + 1)) not in l:
                l.append ((a + 2, b + 1))
                d[(a + 2, b + 1)] = 0
        if a < m and 2 < b <= n:
            if ((a + 1, b - 2)) not in l:
                l.append ((a + 1, b - 2))
                d[(a + 1, b - 2)] = 0
    l = sorted (l)
    for j in range (1, len (l)):
        a = l[j][0]
        b = l[j][1]
        c = l[j]
        x = 0
        y = 0
        z = 0
        w = 0
        if (a - 1, b - 2) in d:
            x = d[(a - 1, b - 2)] * 2
        if (a - 2, b - 1) in d:
            y = d[(a - 2, b - 1)] * 2
        if (a - 1, b + 2) in d:
            z = d[(a - 1, b + 2)] * 2
        if (a - 2, b + 1) in d:
            w = d[(a - 2, b + 1)] * 2

        d[a, b] = x + y + z + w
    return d[point[0]+1,point[1]+1]
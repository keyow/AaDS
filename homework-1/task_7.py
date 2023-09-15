def mul_others(a):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    :param a: Numbers list.
    :return: List. Every number of list is the multiplication of other numbers from that list.
    """
    result = []
    tmp = 1
    for i in range(0, len(a)):
        result.append(tmp)
        if i != len(a) - 1:
            tmp *= a[i]

    tmp = a[-1]
    for i in range(len(a) - 2, -1, -1):
        result[i] *= tmp
        tmp *= a[i]

    return result


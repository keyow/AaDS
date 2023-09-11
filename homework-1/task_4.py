def find_missed(a):
    """
    Complexity: O(n)
    :param a: List, containing all numbers from 0 to n instead of one.
    :return: Missed number.
    """
    if not isinstance(a, list):
        raise TypeError("Input must be a list!")

    return sum([i for i in range(0, len(a) + 1)]) - sum(a)


def find_missed_xor(a):
    """
    Using xor of all elements and xor of all numbers from 0 to n. Xor of these two xors is the missed number.
    Complexity: O(n).
    :param a: List, containing all numbers from 0 to n instead of one.
    :return: Missed number.
    """
    xor = 0
    for el in a:
        xor ^= el
    for i in range(1, len(a) + 1):
        xor ^= i
    return xor

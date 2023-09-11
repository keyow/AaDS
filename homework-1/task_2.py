def find_unique_count(arr):
    """
    Universal function.
    :param arr:
    :return:
    """
    return len(set(arr))


def find_unique_count_positive_only(arr):
    """
    Works only with zeros and positive numbers
    :param arr: Initial array
    :return: Quantity of unique numbers in the array.
    """
    checker = 0
    for el in arr:
        if el < 0:
            raise ValueError("Value can't be negative")
        checker |= (1 << el)
    return checker.bit_count()


print(find_unique_count([1, 2, 3, 3, 4, -1]))

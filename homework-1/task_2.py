def find_unique_count(arr):
    """
    Finds the quantity of numbers used in the array. Converts array to set and gets set's size.
    Time complexity: O(N)
    Space complexity: O(N)
    :param arr:
    :return:
    """
    return len(set(arr))


def find_unique_count_raw(arr, k):
    """
    Finds the quantity of numbers used in the array. Uses basic python arrays (lists) with indexes.
    Space complexity: O(N)
    Time complexity: O(N)
    :param arr: Initial array. Size is N.
    :param k: Maximum value of an array. Values are starting from 1.
    :return: Counter of unique elements.
    """
    used = [1] * k
    counter = 0
    for el in arr:
        counter += used[el - 1]
        used[el - 1] = 0
    return counter


def find_unique_count_positive_only(arr):
    """
    Finds the quantity of numbers used in the array. Works only with zeros and positive numbers.
    Binary checkers is used.
    Time complexity: O(N)
    Space complexity: O(1)
    :param arr: Initial array
    :return: Quantity of unique numbers in the array.
    """
    checker = 0
    for el in arr:
        if el < 0:
            raise ValueError("Value can't be negative")
        checker |= (1 << el)
    return checker.bit_count()


def find_not_repeated_count(arr):
    """
    Finds quantity of numbers which are not repeated inside an array.
    Maximum value (k) is not given (array is randomized).
    Time complexity: O(n*log(n))
    Space complexity: O(n)
    :param arr:
    :return:
    """
    sorted_arr = sorted(arr)
    flag = 1
    c = 1
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] != sorted_arr[i - 1]:
            c += 1
            flag = 1
        else:
            c -= flag
            flag = 0
    return c


print(find_unique_count([1, 2, 3, 3, 4, -1]))
print(find_unique_count([1, 2, 3, 3, 4, 4]))
print(find_not_repeated_count([1, 2, 3, 3, 4, 4, 5, 5]))

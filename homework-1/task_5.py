def find_in_sorted_2D(arr, num):
    """
    Simple binary search algorithm. Starting from the top left and right corner.
    Complexity: O(log(N * M)), where N is number if rows, M is number of columns.
    :param arr: Initial array.
    :param num: Number to find.
    :return: (x, y) coordinates if found, otherwise False.
    """
    i = 0
    j = len(arr) - 1
    while i < len(arr) and j > -1:
        if arr[i][j] == num:
            return i, j
        if num < arr[i][j]:
            j -= 1
        else:
            i += 1
    return False


def find_in_sorted_2D_optimized(arr, num):
    """
    Optimized binary search. Starting from the center of 2D array. If centered element is bigger, searching
    for smaller element, and vice versa. After that splitting array into two sectors and performing
    binary search on both of them.
    Complexity: ? TODO: calculate complexity
    :param arr:
    :param num:
    :return:
    """
    n = len(arr)
    m = len(arr[0])

    i, j = n // 2, m // 2
    if num > arr[i][j]:
        while num > arr[i][j] and i < n - 1 and j < m - 1:
            i += 1
            j += 1
            if arr[i][j] == num:
                return i, j
    elif num < arr[i][j]:
        while num < arr[i][j] and i > 0 and j > 0:
            i -= 1
            j -= 1
            if arr[i][j] == num:
                return i, j
    else:
        return i, j

    right_sector_i = 0
    right_sector_j = len(arr) - 1
    while right_sector_i < i and right_sector_j > j - 1:
        if arr[right_sector_i][right_sector_j] == num:
            return right_sector_i, right_sector_j
        if num < arr[right_sector_i][right_sector_j]:
            right_sector_j -= 1
        else:
            right_sector_i += 1

    left_sector_i = i
    left_sector_j = j - 1
    while left_sector_i < len(arr) and left_sector_j > -1:
        if arr[left_sector_i][left_sector_j] == num:
            return left_sector_i, left_sector_j
        if num < arr[left_sector_i][left_sector_j]:
            left_sector_j -= 1
        else:
            left_sector_i += 1

    return False

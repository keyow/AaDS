def find_in_sorted_2D(arr, num):
    """
    Simple binary search algorithm. Starting from the top left and right corner.
    Space complexity: O(1)
    Time complexity: O(log(N + M)), where N is number if rows, M is number of columns.
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

def find_min(arr):
    """
    Initial array is shifted by N (N is unknown)
    Time complexity: O(log(N))
    :return: minimal element
    """
    if not arr:
        return 0
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) >> 1
        if arr[left] > arr[mid]:
            right = mid
        elif arr[right] < arr[mid]:
            left = mid + 1
        else:
            return arr[left]
    return arr[left]


# Ограничения:
# 1. Крайний левый, крайний правый и серединный не равны
# 2. Не распространяется на последовательность длины 3

print(find_min([5, 0, 5, 5, 5, 5, 5, 5]))  # WRONG
print(find_min([4, 5, 6, 7, 8, 100, -1, 0]))
print(find_min([4, 5, 6, 7, 8, 100, 109, -1]))

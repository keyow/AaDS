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
        if right - left > 2 and arr[left] == arr[right] == arr[mid]:
            minimal = arr[0]
            for i in range(left, mid):
                if arr[i] < minimal:
                    minimal = arr[i]
            if minimal == arr[0]:
                left = mid
                continue
            return minimal
        else:
            if arr[left] > arr[mid]:
                right = mid
            elif arr[right] < arr[mid]:
                left = mid + 1
            else:
                return arr[left]
    return arr[left]


print(find_min([5, 5, 4, 5, 5]))
print(find_min([5, 5, 5, 5, 5, 5, 5, 1, 5, 5]))
print(find_min([8, 8, 0, 5, 8, 8, 8, 8, 8, 8]))
print(find_min([5, 5, 4, 4, 5, 5, 5]))
print(find_min([4, 5, 6, 7, 8, 100, -1, 0]))
print(find_min([4, 5, 6, 7, 8, 100, 109, -1]))
print(find_min([1, 3, 4, 5, 6, 7, 8, 9]))
print(find_min([7, 10, 2, 4, 5, 6]))
print(find_min([0, 5, 5, 5, 5, 5]))
print(find_min([5, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
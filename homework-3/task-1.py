def find_peak(arr):
    left = 0
    right = len(arr) - 1
    while left != right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left


print(find_peak([1, 2, 3, 2, 6, 7, 8, 3]))
print(find_peak([10, 2, 3, 4, 1, 7, 8, 3]))
print(find_peak([10]))
print(find_peak([10, 1]))
print(find_peak([10, 215]))
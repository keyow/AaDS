def bin_search(arr, value):
    begin = 0
    end = len(arr) - 1

    while begin != end:
        print(begin, end)
        mid = (begin + end) // 2
        if arr[mid] == value:
            return mid
        if arr[mid] > value:
            end = mid
        else:
            begin = mid + 1
    return -1


print(bin_search([1, 2, 4, 6, 10], 10))
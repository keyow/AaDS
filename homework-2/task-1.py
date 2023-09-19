def sublist_sum(arr, m):
    n = len(arr)
    if m > n or m <= 0:
        return False

    result = []
    s = 0
    for i in range(0, m):
        s += arr[i]
    result.append(s)
    for i in range(m, n):
        s -= arr[i - m]
        s += arr[i]
        result.append(s)
    return result


print(sublist_sum([1, 6, 78, 12, 5], 3))
def calc__time(queue, k):
    total_time = 0
    for i in range(len(queue)):
        if i <= k:
            total_time += min(queue[i], queue[k])
        elif i > k:
            total_time += min(queue[i], queue[k] - 1)
    return total_time


print(calc__time([1, 1, 1, 1, 1, 1, 10, 11], 6))

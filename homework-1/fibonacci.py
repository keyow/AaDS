def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = [0, 1] + [0] * (n - 1)
    for i in range(2, len(a)):
        a[i] = a[i - 1] + a[i - 2]
    return a[n]

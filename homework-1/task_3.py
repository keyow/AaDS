def denominator_fact_sum(n):
    numerator = 0
    denominator = 1
    for i in range(n, 0, -1):
        numerator += denominator
        denominator *= i
    return numerator / denominator


print(denominator_fact_sum(5))

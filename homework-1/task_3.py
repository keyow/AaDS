def denominator_fact_sum(n):
    """
    Finds result of expression:
    1 / 1! + 1 / 2! + 1 / 3! + ... + 1 / n!
    Space complexity: O(1)
    Time complexity: O(N)
    :param n: Specified value
    :return: Expression value
    """
    numerator = 0
    denominator = 1
    for i in range(n, 0, -1):
        numerator += denominator
        denominator *= i
    return numerator / denominator


print(denominator_fact_sum(1))

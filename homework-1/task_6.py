def validate_sudoku_rapid(field, n):
    """
    Validates the sudoku field. Some cells may be unfilled.
    Time complexity: O(N^2)
    Space complexity: O(1)
    :param n: Sudoku inner field size.
    :param field: Sudoku field. Size is NxN (N = n^2, where n is a size of the inner square)
    :return: Boolean. True if field is valid, otherwise False.
    """
    N = len(field)
    calculated_N = n ** 2
    if len(field) != calculated_N:
        return False
    for row in field:
        if len(row) != calculated_N:
            return False

    # Checking rows
    checker = 0  # binary checker
    for row in field:
        for el in row:
            if el != 0:
                if checker & (1 << el) != 0:
                    return False
                checker |= 1 << el
        checker = 0

    # Checking columns
    checker = 0
    for j in range(N):
        for row in field:
            if row[j] != 0:
                if checker & (1 << row[j]) != 0:
                    return False
                checker |= 1 << row[j]
        checker = 0

    # Checking squares
    checker = 0
    for square_i in range(n):
        for square_j in range(n):
            for i in range(n):
                for j in range(n):
                    f_i, s_i = square_i * n + i, square_j * n + j
                    if field[f_i][s_i] != 0:
                        if checker & (1 << field[f_i][s_i]) != 0:
                            return False
                    checker |= 1 << field[f_i][s_i]
            checker = 0

    return True

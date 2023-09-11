def validate_sudoku_solution(field, n):
    """
    Validates the sudoku field.
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

    total = sum(range(1, N + 1))

    # Checking rows
    for row in field:
        if sum(row) != total:
            return False

    # Checking columns
    for j in range(N):
        col_sum = 0
        for row in field:
            col_sum += row[j]
            if col_sum > total:
                return False

    # Checking squares
    square_total = 0
    for square_i in range(n):
        for square_j in range(n):
            for i in range(n):
                for j in range(n):
                    square_total += field[square_i * n + i][square_j * n + j]
            if square_total != total:
                return False
            square_total = 0

    return True


def validate_sudoku_solution_optimized(field, n):
    """
    Validates the sudoku field. Optimized because of additional memory space.
    Time complexity: O(N^2)
    Space complexity: O(N)
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

    total = sum(range(1, N + 1))
    squares_line_total = {i: 0 for i in range(n)}  # Space: O(N)
    columns_total = {i: 0 for i in range(N)}  # Space: O(N)

    square_i, square_j = 0, 0
    for i in range(N):
        line_total = 0
        for j in range(N):
            line_total += field[i][j]
            columns_total[j] += field[i][j]
            squares_line_total[square_j] += field[i][j]
            if j == N - 1:
                square_j = 0
            elif j == square_j * n + n - 1:
                square_j += 1
        if line_total != total:
            return False
        if i == square_i * n + n - 1:
            for square_total in squares_line_total.values():
                if square_total != total:
                    return False
            squares_line_total = {i: 0 for i in range(n)}
            square_i += 1

    for column_total in columns_total.values():
        if column_total != total:
            return False

    return True


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


import unittest
from random import sample, randint
from fibonacci import fibonacci
from fast_fibonacci import fast_fibonacci
from task_4 import find_missed, find_missed_xor
from task_5 import find_in_sorted_2D, find_in_sorted_2D_optimized
from task_6 import validate_sudoku_rapid
from task_7 import mul_others


class FibonacciTests(unittest.TestCase):
    def test_fibonacci(self):
        for i in range(0, 50):
            self.assertEqual(fibonacci(i), fast_fibonacci(i))


class Task4Tests(unittest.TestCase):
    def test_find_missed(self):
        arr = sample(range(0, 100), 100)  # generate list of 100 random numbers in [0, 99] segment
        pos = randint(0, 99)
        deleted_element = arr[pos]
        del arr[pos]
        self.assertEqual(deleted_element, find_missed(arr))
        self.assertEqual(deleted_element, find_missed_xor(arr))


class Task5Tests(unittest.TestCase):
    def test_find_in_sorted(self):
        size = 100
        min_delta = 0
        max_delta = 10
        arr = [[0 for j in range(size)] for i in range(size)]
        arr[0][0] = randint(min_delta, max_delta)

        for i in range(1, size):
            arr[i][0] = arr[i - 1][0] + randint(min_delta, max_delta)
        for j in range(1, size):
            arr[0][j] = arr[0][j - 1] + randint(min_delta, max_delta)
        for i in range(size):
            for j in range(size):
                arr[i][j] = max(arr[i][j - 1], arr[i - 1][j]) + randint(min_delta, max_delta)

        i = randint(0, size - 1)
        j = randint(0, size - 1)
        target = arr[i][j]

        found_coords = find_in_sorted_2D(arr, target)
        self.assertNotEqual(found_coords, False)
        self.assertEqual(target, arr[found_coords[0]][found_coords[1]])

        found_coords = find_in_sorted_2D_optimized(arr, target)
        self.assertNotEqual(found_coords, False)
        self.assertEqual(target, arr[found_coords[0]][found_coords[1]])

        target = min_delta - 100
        self.assertFalse(find_in_sorted_2D(arr, target))
        self.assertFalse(find_in_sorted_2D_optimized(arr, target))


class Task6Tests(unittest.TestCase):
    def test_validate_sudoku_filled(self):
        sudoku = [[9, 7, 6, 4, 8, 1, 3, 2, 5],
                  [1, 4, 3, 2, 5, 9, 7, 8, 6],
                  [5, 2, 8, 3, 7, 6, 1, 9, 4],
                  [6, 9, 4, 5, 1, 8, 2, 3, 7],
                  [8, 1, 2, 7, 3, 4, 5, 6, 9],
                  [7, 3, 5, 9, 6, 2, 4, 1, 8],
                  [4, 6, 7, 8, 2, 3, 9, 5, 1],
                  [2, 5, 1, 6, 9, 7, 8, 4, 3],
                  [3, 8, 9, 1, 4, 5, 6, 7, 2]]

        self.assertTrue(validate_sudoku_rapid(sudoku, 3))

        sudoku[5][5] = 4
        sudoku[5][6] = 4
        self.assertFalse(validate_sudoku_rapid(sudoku, 3))


class Task7Tests(unittest.TestCase):
    def test_mul_others(self):
        arr = [1, 5, 2, 5, 3, 10]
        self.assertEqual([1500, 300, 750, 300, 500, 150], mul_others(arr))

        arr = [10]
        self.assertEqual([1], mul_others(arr))


if __name__ == '__main__':
    unittest.main()

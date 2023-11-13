import unittest
import os
from subprocess import Popen, PIPE


class SplayTreeTest(unittest.TestCase):
    def setUp(self):
        self.TEST_QUANTITY = len(os.listdir('tests/task_1/testcases'))
        assert self.TEST_QUANTITY == len(os.listdir('tests/task_1/answers'))

    def test_splay_tree(self):
        for test_id in range(1, self.TEST_QUANTITY + 1):
            print(test_id)
            try:
                with open(f'tests/task_1/answers/ans_{test_id}.txt', 'r') as answer:
                    expected = answer.read()
                with open(f'tests/task_1/testcases/test_{test_id}.txt', 'r') as testcase:
                    p = Popen(['python', 'task_1_splay.py'], stdout=PIPE, stdin=PIPE)
                    p.stdin.write(testcase.read().encode())
                    output = p.communicate()[0]
                    self.assertEqual(expected, output.decode().replace('\r', ''))
            except IOError as e:
                print(e)


class HeapTest(unittest.TestCase):
    def setUp(self):
        self.TEST_QUANTITY = len(os.listdir('tests/task_2/testcases'))
        assert self.TEST_QUANTITY == len(os.listdir('tests/task_2/answers'))

    def test_heap(self):
        for test_id in range(1, self.TEST_QUANTITY + 1):
            print(test_id)
            try:
                with open(f'tests/task_2/answers/ans_{test_id}.txt', 'r') as answer:
                    expected = answer.read()
                with open(f'tests/task_2/testcases/test_{test_id}.txt', 'r') as testcase:
                    p = Popen(['python', 'task_2_heap.py'], stdout=PIPE, stdin=PIPE)
                    p.stdin.write(testcase.read().encode())
                    output = p.communicate()[0]
                    self.assertEqual(expected, output.decode().replace('\r', ''))
            except IOError as e:
                print(e)


class MistakeSolverTest(unittest.TestCase):
    def setUp(self):
        self.TEST_QUANTITY = len(os.listdir('tests/task_3/testcases'))
        assert self.TEST_QUANTITY == len(os.listdir('tests/task_3/answers'))

    def test_mistake_solver(self):
        for test_id in range(1, self.TEST_QUANTITY + 1):
            print(test_id)
            try:
                with open(f'tests/task_3/answers/ans_{test_id}.txt', 'r', encoding='utf-8') as answer:
                    expected = answer.read()
                with open(f'tests/task_3/testcases/test_{test_id}.txt', 'r', encoding='utf-8') as testcase:
                    p = Popen(['python', 'task_3_mistakes.py'], stdout=PIPE, stdin=PIPE)
                    p.stdin.write(testcase.read().encode('utf-8'))
                    output = p.communicate()[0]
                    self.assertEqual(expected, output.decode('utf-8').replace('\r', ''))
            except IOError as e:
                print(e)


if __name__ == '__main__':
    unittest.main()

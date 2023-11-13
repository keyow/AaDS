import unittest
import os
from collections import Counter
from module_1.ejudge.wip.task_3_fast_wip import find_parents, find_chains


class LibSearchTest(unittest.TestCase):
    def setUp(self):
        self.TEST_QUANTITY = len(os.listdir('task_3_tests/testcases'))
        assert self.TEST_QUANTITY == len(os.listdir('task_3_tests/answers'))

    def test_libsearch(self):
        for test_id in range(1, self.TEST_QUANTITY + 1):
            try:
                with open(f'ejudge/task_3_tests/answers/test_{test_id}_ans.txt', 'r') as answer:
                    expected = [tuple(line.split()) for line in answer.readlines()]
                with open(f'ejudge/task_3_tests/testcases/test_{test_id}.txt', 'r') as testcase:
                    vulnerable_targets = testcase.readline().split()
                    own_libraries = testcase.readline().split()
                    libs_parents = find_parents(testcase.readlines())
                    result = list()
                    for target in vulnerable_targets:
                        found_chains = find_chains(target, libs_parents, own_libraries)
                        for c in found_chains:
                            result.append(tuple(c))
                self.assertEqual(Counter(expected), Counter(result))
            except IOError as e:
                print(e)


if __name__ == '__main__':
    unittest.main()

import re
import sys


def find_sum(s):
    result = 0
    for element in re.findall(r'-?\d+', s):
        result += int(element)
    return result


print(find_sum(sys.stdin.read()))

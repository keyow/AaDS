import re
import sys


class Heap:
    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value

        def __lt__(self, other):
            return self.key < other.key

        def __gt__(self, other):
            return self.key > other.key

    def __init__(self):
        self.__indexes = {}
        self.data = []

    def __swap_nodes(self, i, j):
        if i == j:
            return
        self.data[i], self.data[j] = self.data[j], self.data[i]

        first = self.data[i].key
        second = self.data[j].key
        self.__indexes[first], self.__indexes[second] = self.__indexes[second], self.__indexes[first]

    def __sift_up(self, i):
        while i > 0 and self.data[i] < self.data[(i - 1) // 2]:
            j = (i - 1) // 2
            self.__swap_nodes(i, j)
            i = j

    def __sift_down(self, i):
        while 2 * i + 1 < self.size():
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < self.size() and self.data[right] < self.data[left]:
                j = right
            if self.data[i] < self.data[j]:
                break
            self.__swap_nodes(i, j)
            i = j

    def size(self):
        return len(self.data)

    def add(self, key, value):
        if key in self.__indexes:
            raise IndexError("error")
        self.data.append(self.Node(key, value))
        self.__indexes[key] = self.size() - 1
        self.__sift_up(self.size() - 1)

    def set(self, key, value):
        if key not in self.__indexes:
            raise IndexError("error")
        self.data[self.__indexes[key]].value = value

    def delete(self, key):
        if key not in self.__indexes:
            raise IndexError("error")
        key_index = self.__indexes[key]
        self.__swap_nodes(key_index, self.size() - 1)

        self.data.pop()
        del self.__indexes[key]

        if key_index != self.size():
            self.__sift_down(key_index)
            self.__sift_up(key_index)

    def search(self, key):
        if key in self.__indexes:
            return self.data[self.__indexes[key]]
        return 0

    def get_index(self, key):
        return self.__indexes[key]

    def get_by_index(self, idx):
        return self.data[idx]

    def extract(self):
        if not self.data:
            raise IndexError("error")
        node = self.data[0]
        self.delete(node.key)
        return node

    def min(self):
        if not self.data:
            raise IndexError("error")
        return self.data[0]

    def max(self):
        if not self.data:
            raise IndexError("error")
        maximum_node = self.data[self.size() // 2]
        for i in range(self.size() // 2 + 1, self.size()):
            if self.data[i] > maximum_node:
                maximum_node = self.data[i]
        return maximum_node


def print_heap(heap):
    if not heap.data:
        print('_')
        return

    node = heap.get_by_index(0)
    print(f'[{node.key} {node.value}]')

    for i in range(1, heap.size()):
        node = heap.get_by_index(i)
        parent_node = heap.get_by_index((i - 1) // 2)
        if (i + 2) & (i + 1) == 0:
            print(f'[{node.key} {node.value} {parent_node.key}]', end='\n')
        else:
            print(f'[{node.key} {node.value} {parent_node.key}]', end=' ')
    end = 2 ** heap.size().bit_length() - 1
    if heap.size() < end:
        print((end - heap.size() - 1) * '_ ', end='_\n')


class CommandParser:
    def __init__(self):
        self.match = None

    def parse(self, p, c):
        self.match = re.search(p, c)
        return self.match

    def get_value(self, i):
        if not self.match:
            return None
        return self.match.group(i)


if __name__ == "__main__":
    heap = Heap()

    parser = CommandParser()
    for command in sys.stdin.readlines():
        try:
            if parser.parse(r"^add\s(-?\d+)\s(.*?)$", command):
                heap.add(int(parser.get_value(1)), parser.get_value(2))
            elif parser.parse(r"^search\s(-?\d+)$", command):
                searched = heap.search(int(parser.get_value(1)))
                if searched:
                    print(f'1 {heap.get_index(searched.key)} {searched.value}')
                else:
                    print(0)
            elif parser.parse(r"^set\s(-?\d+)\s(.*?)$", command):
                heap.set(int(parser.get_value(1)), parser.get_value(2))
            elif parser.parse(r"^delete\s(-?\d+)$", command):
                heap.delete(int(parser.get_value(1)))
            elif parser.parse(r"^print$", command):
                print_heap(heap)
            elif parser.parse(r"^min$", command):
                min_node = heap.min()
                print(f"{min_node.key} 0 {min_node.value}")
            elif parser.parse(r"^max$", command):
                max_node = heap.max()
                print(f"{max_node.key} {heap.get_index(max_node.key)} {max_node.value}")
            elif parser.parse("^extract$", command):
                heap_top = heap.extract()
                print(f"{heap_top.key} {heap_top.value}")
            elif command != '\n':
                raise NameError("error")
        except (IndexError, NameError) as e:
            print(e)

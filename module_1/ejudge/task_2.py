import sys
import re


class Dequeue:
    def __init__(self, capacity=0):
        if capacity is None:
            capacity = 0
        self._capacity = capacity + 1
        self._head = 0
        self._tail = 0
        self._d = [0] * (capacity + 1)

    def push_front(self, val):
        if self.full():
            raise OverflowError('overflow')
        self._head = (self._head - 1 + self._capacity) % self._capacity
        self._d[self._head] = val

    def push_back(self, val):
        if self.full():
            raise OverflowError('overflow')
        self._d[self._tail] = val
        self._tail = (self._tail + 1) % self._capacity

    def pop_front(self):
        if self.empty():
            raise OverflowError('underflow')
        val = self._d[self._head]
        self._head = (self._head + 1) % self._capacity
        print(val)
        return val

    def pop_back(self):
        if self.empty():
            raise OverflowError('underflow')
        self._tail = (self._tail - 1) % self._capacity
        print(self._d[self._tail])
        return self._d[self._tail]

    def print(self):
        if self.empty():
            print('empty')
            return
        idx = self._head
        while idx != self._tail:
            print(self._d[idx], end='')
            idx = (idx + 1) % self._capacity
            if idx != self._tail:
                print(' ', end='')
        print()

    def full(self):
        return self._head == (self._tail + 1) % self._capacity

    def empty(self):
        return self._head == self._tail


class CommandParser:
    def __init__(self):
        self.match = None

    def parse(self, p, c):
        self.match = re.search(p, c)
        return self.match

    def get_value(self):
        if not self.match:
            return None
        return self.match.group(1)


commands = sys.stdin.readlines()
parser = CommandParser()

dequeue = None
for i in range(len(commands)):
    command = commands[i]
    try:
        if command == '\n':
            continue
        elif parser.parse(r"^set_size\s(\d+)$", command):
            if dequeue is not None:
                raise ValueError('error')
            dequeue = Dequeue(int(parser.get_value()))
        elif dequeue is None:
            raise ValueError('error')
        elif parser.parse(r"^pushf\s(\S+)$", command):
            dequeue.push_front(parser.get_value())
        elif parser.parse(r"^pushb\s(\S+)$", command):
            dequeue.push_back(parser.get_value())
        elif parser.parse("^popf$", command):
            dequeue.pop_front()
        elif parser.parse("^popb$", command):
            dequeue.pop_back()
        elif parser.parse("^print$", command):
            dequeue.print()
        else:
            raise ValueError('error')
    except (OverflowError, ValueError) as e:
        print(e)

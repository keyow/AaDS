from random import randint


class Node:
    def __init__(self, data=None, nxt=None):
        self._data = data
        self._next = nxt

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @data.setter
    def data(self, d):
        self._data = d

    @next.setter
    def next(self, nxt):
        self._next = nxt


def get_list(node):
    l = []
    while node:
        l.append(node.data)
        node = node.next
    return l


def reverse_from_second(node):
    current_node = node.next
    if current_node is None:
        return

    prev = None
    while current_node:
        next_node = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = next_node
    node.next = prev


head = Node(randint(0, 10))
cur_node = head
for i in range(25):
    new_node = Node(randint(0, 10))
    cur_node.next = new_node
    cur_node = new_node

print(get_list(head))
reverse_from_second(head)
print(get_list(head))
import sys
import re


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    def __init__(self, root=None):
        self.root = root

    def __right_rotation(self, x):
        z = x.left

        z.parent = x.parent
        if x.parent is None:
            self.root = z
        elif x.parent.left == x:
            x.parent.left = z
        else:
            x.parent.right = z
        x.parent = z

        x.left = z.right
        if z.right is not None:
            z.right.parent = x

        z.right = x

    def __left_rotation(self, x):
        z = x.right

        z.parent = x.parent
        if x.parent is None:
            self.root = z
        elif x.parent.left == x:
            x.parent.left = z
        else:
            x.parent.right = z
        x.parent = z

        x.right = z.left
        if z.left is not None:
            z.left.parent = x

        z.left = x

    def __splay(self, x):
        while x.parent is not None:
            if x.parent.parent is None:
                if x.parent.left == x:
                    self.__right_rotation(x.parent)
                else:
                    self.__left_rotation(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self.__right_rotation(x.parent.parent)
                self.__right_rotation(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self.__left_rotation(x.parent.parent)
                self.__left_rotation(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.right:
                self.__right_rotation(x.parent)
                self.__left_rotation(x.parent)
            else:
                self.__left_rotation(x.parent)
                self.__right_rotation(x.parent)

    def __search_tree(self, key):
        prev = None
        node = self.root

        while node is not None and node.key != key:
            prev = node
            if key < node.key:
                node = node.left
            else:
                node = node.right
        if node is None:
            return prev
        return node

    def __maximum(self, node=None):
        if self.root is None:
            raise IndexError("error")
        if node is None:
            node = self.root

        while node.right is not None:
            node = node.right
        return node

    def __minimum(self, node=None):
        if self.root is None:
            raise IndexError("error")
        if node is None:
            node = self.root

        while node.left is not None:
            node = node.left
        return node

    def delete(self, key):
        node = self.__search_tree(key)
        if node is None:
            raise IndexError("error")

        self.__splay(node)
        if node.key != key:
            raise IndexError("error")

        if node.left is None and node.right is None:
            self.root = None
            return

        if node.right is None:
            node.left.parent = None
            self.root = node.left
            return
        node.right.parent = None

        if node.left is None:
            self.root = node.right
            return
        node.left.parent = None

        new_root = self.__maximum(node.left)
        self.__splay(new_root)

        new_root.right = node.right
        node.right.parent = new_root

        del node

    def maximum(self):
        max_node = self.__maximum()
        self.__splay(max_node)
        return max_node

    def minimum(self):
        min_node = self.__minimum()
        self.__splay(min_node)
        return min_node

    def insert(self, key, data):
        node = Node(key, data)

        prev = None
        x = self.root
        while x is not None and x.key != key:
            prev = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        if x is not None and x.key == key:
            self.__splay(x)
            raise ValueError("error")

        node.parent = prev
        if prev is None:
            self.root = node
        elif node.key <= prev.key:
            prev.left = node
        else:
            prev.right = node
        self.__splay(node)

    def search(self, key):
        node = self.__search_tree(key)

        if node:
            self.__splay(node)
            if node.key == key:
                return node
        return None

    def set(self, key, data):
        node = self.__search_tree(key)

        if node is None:
            raise IndexError("error")
        self.__splay(node)
        if node.key != key:
            raise IndexError("error")
        if node.key == key:
            node.data = data


def print_tree(cur_node):
    if cur_node:
        print(f'[{cur_node.key} {cur_node.data}]')
    else:
        print('_')
        return

    layer = {}
    next_layer = {}

    if cur_node.left:
        layer[0] = cur_node.left
    if cur_node.right:
        layer[1] = cur_node.right

    size = 2
    while layer:
        prev_index = -1
        for index in layer:
            cur_node = layer[index]
            if index == 0:
                print(f'[{cur_node.key} {cur_node.data} {cur_node.parent.key}]', end='')
            else:
                if prev_index == -1:
                    print((index - 1) * '_ ', end='_')
                else:
                    print((index - prev_index - 1) * ' _', end='')
                print(f' [{cur_node.key} {cur_node.data} {cur_node.parent.key}]', end='')
            if cur_node.left:
                next_layer[2 * index] = cur_node.left
            if cur_node.right:
                next_layer[2 * index + 1] = cur_node.right
            prev_index = index
        if prev_index < size - 1:
            print((size - prev_index - 1) * ' _', end='')
        layer = next_layer
        next_layer = {}
        size *= 2
        print()


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
    tree = SplayTree()

    parser = CommandParser()
    for command in sys.stdin.readlines():
        try:
            if command == '\n':
                continue
            elif parser.parse(r"^add\s(-?\d+)\s(.*?)$", command):
                tree.insert(int(parser.get_value(1)), parser.get_value(2))
            elif parser.parse(r"^search\s(-?\d+)$", command):
                searched = tree.search(int(parser.get_value(1)))
                if searched:
                    print(f'1 {searched.data}')
                else:
                    print(0)
            elif parser.parse(r"^set\s(-?\d+)\s(.*?)$", command):
                tree.set(int(parser.get_value(1)), parser.get_value(2))
            elif parser.parse(r"^delete\s(-?\d+)$", command):
                tree.delete(int(parser.get_value(1)))
            elif parser.parse(r"^print$", command):
                print_tree(tree.root)
            elif parser.parse(r"^min$", command):
                minimum = tree.minimum()
                print(f"{minimum.key} {minimum.data}")
            elif parser.parse(r"^max$", command):
                maximum = tree.maximum()
                print(f"{maximum.key} {maximum.data}")
            else:
                raise NameError("error")
        except (IndexError, NameError, ValueError) as e:
            print(e)

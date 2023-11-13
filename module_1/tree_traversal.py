from tree import Node
from queue import Queue

# IN ORDER
def in_order_recursive(node):
    if node:
        in_order_recursive(node.left)
        print(node.data)
        in_order_recursive(node.right)


def in_order_iterative(node):
    stk = []
    result = []
    while True:
        if node:
            stk.append(node)
            node = node.left
        else:
            if not stk:
                break
            node = stk.pop()
            result.append(node.data)
            node = node.right
    return result


# LEVEL ORDER
def level_order_iterative(node):
    if not node:
        return
    queue = Queue()
    queue.put(node)
    result = []
    while not queue.empty():
        node = queue.get()
        result.append(node.data)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
    return result

class Node:
    def __init__(self, d):
        self.data = d
        self.right = None
        self.left = None
        self.parent = None

    def __repr__(self):
        return str(self.data)

import math


class Node(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = None


def insert(root, key, value=None):
    if root is None:
        root = Node(key, value)
    elif key < root.key:
        root.left = insert(root.left, key, value)
    else:
        root.right = insert(root.right, key, value)

    return root


def traverse(node, callback):
    if node is None:
        return
    traverse(node.left, callback)
    callback(node)
    traverse(node.right, callback)


def print_key(node):
    print(node.key)


def print_tree(root):
    traverse(root, print_key)


def verification_recursive(node, min=-math.inf, max=math.inf):
    if node is None:
        return True
    if node.key > min and \
            node.key < max and \
            verification_recursive(node.left, min, node.key) and \
            verification_recursive(node.right, node.key, max):
        return True
    return False


example_tree = Node(8)
insert(example_tree, 3)
insert(example_tree, 10)
insert(example_tree, 1)
insert(example_tree, 6)
insert(example_tree, 14)
insert(example_tree, 4)
insert(example_tree, 7)
insert(example_tree, 13)

print_tree(example_tree)
print(verification_recursive(example_tree))

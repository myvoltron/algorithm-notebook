class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


def preorder(node):
    if node is not None:
        print(node.value, end="")
        if node.left is not None:
            preorder(node.left)
        if node.right is not None:
            preorder(node.right)


def inorder(node):
    if node is not None:
        if node.left is not None:
            inorder(node.left)
        print(node.value, end="")
        if node.right is not None:
            inorder(node.right)


def postorder(node):
    if node is not None:
        if node.left is not None:
            postorder(node.left)
        if node.right is not None:
            postorder(node.right)
        print(node.value, end="")


n = int(input())
nodes = []
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for ch in alpha:
    nodes.append(Node(ch))

while n > 0:
    parent, left, right = input().split()
    if left != ".":
        nodes[ord(parent) - ord("A")].set_left(nodes[ord(left) - ord("A")])
    if right != ".":
        nodes[ord(parent) - ord("A")].set_right(nodes[ord(right) - ord("A")])
    n -= 1

preorder(nodes[0])
print()
inorder(nodes[0])
print()
postorder(nodes[0])

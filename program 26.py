class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def preOrder(root):
    if root:
        # print the current node's data
        print(root.data, end=" ")
        # Recursively traverse the left subtree
        preOrder(root.left)
        # Recursively traverse the right subtree
        preOrder(root.right)
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)
# Calling preOrder function to print the preOrder traversal
print("preOrder Traversal:", end=" ")
preOrder(root)

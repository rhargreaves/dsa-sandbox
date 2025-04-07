class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# original solution
def height(root):

    def walk(node, level):
        left_level = level
        right_level = level
        if node.left:
            left_level = walk(node.left, level + 1)
        if node.right:
            right_level = walk(node.right, level + 1)
        return max(left_level, right_level)

    return walk(root, 0)


# alternative solution
def height2(node):
    if not node.left and not node.right:
        return 0
    left = 0
    right = 0
    if node.left:
        left = height2(node.left)
    if node.right:
        right = height2(node.right)
    return max(left, right) + 1


# slick solution!
def height3(node):
    if not node:
        return -1
    return max(height3(node.left), height3(node.right)) + 1


tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    tree.create(arr[i])
print(height(tree.root))

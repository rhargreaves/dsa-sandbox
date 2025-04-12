import sys


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


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''


def debug(context='', **kwargs):
    print((context + ": " if context else '') +
          ' '.join(f"{k}={v}" for k, v in kwargs.items()), file=sys.stderr)


def lca(root, v1, v2):
    v1_crumbs = {}
    v2_crumbs = {}
    debug(v1=v1, v2=v2)

    def walk(node, find_val, crumbs):
        debug("walk", find_val=find_val)
        if node.info == find_val:
            debug("found val")
            return node
        found_node = None
        if node.left:
            debug("walking left")
            crumbs[node.left.info] = node
            found_node = walk(node.left, find_val, crumbs)
        if not found_node and node.right:
            debug("walking right")
            crumbs[node.right.info] = node
            found_node = walk(node.right, find_val, crumbs)
        return found_node

    final_v1 = walk(root, v1, v1_crumbs)
    final_v2 = walk(root, v2, v2_crumbs)

    debug(final_v1=final_v1.info,
          final_v2=final_v2.info,
          v1_crumbs=v1_crumbs,
          v2_crumbs=v2_crumbs)

    def visited(crumbs, final_node):
        visited = []
        node = final_node
        while True:
            visited.insert(0, node)
            if node.info in crumbs:
                node = crumbs[node.info]
            else:
                break
        return visited

    v1_visited = visited(v1_crumbs, final_v1)
    v2_visited = visited(v2_crumbs, final_v2)

    debug(v1_visited=[n.info for n in v1_visited],
          v2_visited=[n.info for n in v2_visited])

    lca = None
    for i in range(min(len(v1_visited), len(v2_visited))):
        if v1_visited[i] == v2_visited[i]:
            lca = v1_visited[i]

    return lca


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)

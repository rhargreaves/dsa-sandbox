from collections import defaultdict
import sys
import heapq
import queue


def debug_print(text):
    print(text, file=sys.stderr)


class Graph:
    def __init__(self, num_nodes):
        debug_print(f"new graph! num nodes = {num_nodes}\n")
        self.num_nodes = num_nodes
        self.connections = defaultdict(lambda: [])

    def connect(self, x, y):
        self.connections[x].append(y)
        self.connections[y].append(x)
        debug_print(f"connecting {x} <-> {y}\n")
        return

    def find_all_distances(self, start_node):
        debug_print(f"find_all_distances - start={start_node}")
        distances = [-1] * self.num_nodes
        visited = set()
        unvisited = queue.Queue()
        unvisited.put((0, start_node))

        while not unvisited.empty():
            dist, node = unvisited.get()
            if node in visited:
                continue
            distances[node] = dist
            visited.add(node)

            next_nodes = self.connections[node]
            for next_node in next_nodes:
                new_dist = dist + 6
                unvisited.put((new_dist, next_node))

        print(" ".join([str(i) for i in distances if i != 0]))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x-1, y-1)
    s = int(input())
    graph.find_all_distances(s-1)

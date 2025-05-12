# solution for https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

from collections import defaultdict
import sys
import heapq


def debug_print(text):
    print(text, file=sys.stderr)


class Graph:
    def __init__(self, num_nodes):
        debug_print(f"new graph! num nodes = {num_nodes}")
        self.num_nodes = num_nodes
        self.connections = defaultdict(lambda: [])

    def connect(self, x, y):
        self.connections[x].append(y)
        self.connections[y].append(x)
        debug_print(f"connecting {x} <-> {y}")
        return

    def find_all_distances(self, start_node):
        debug_print(f"find_all_distances - start={start_node}")
        distances = [-1] * self.num_nodes
        visited = set()
        unvisited = []
        # actually a min-heap is not necessary here as all distances are the same
        # can just be a queue! (see bfs_2.py)
        heapq.heappush(unvisited, (0, start_node))
        distances[start_node] = 0

        while unvisited:
            weight, node = heapq.heappop(unvisited)
            if node in visited:
                continue
            visited.add(node)
            distances[node] = weight
            next_nodes = self.connections[node]
            for next_node in next_nodes:
                new_weight = weight + 6
                heapq.heappush(unvisited, (new_weight, next_node))

        print(" ".join([str(i) for i in distances if i != 0]))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)

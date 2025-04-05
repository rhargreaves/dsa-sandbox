from dataclasses import dataclass
from heapq import heappop, heappush
import sys

INF = sys.maxsize


@dataclass
class Node:
    label: str
    weight: int
    neighbours: list['Edge']
    prev: 'Node' = None   # optional: for tracking back to build the shortest path!

    def __lt__(self, other):
        self.weight < other.weight


@dataclass
class Edge:
    weight: int
    node: Node


def find_shortest_path(startNode, goalNode) -> tuple[int, list[str]]:
    visited = set()  # O(1) - efficient checking to ensure don't process nodes twice
    unvisited = []
    heappush(unvisited, (startNode.weight, startNode))  # this is enough! we'll add them as we "see them"

    while unvisited:
        node = heappop(unvisited)[1]

        if node.label in visited:
            print(f"*** Already visited {node.label}. Skipping")
            continue

        visited.add(node.label)

        print(f"*** Visited Node {node.label} from {
            node.prev.label if node.prev else None} weight = {node.weight}\n")

        if node == goalNode:
            print("*** Visited goal node. Ending.")
            break

        for c in node.neighbours:
            new_weight = c.weight + node.weight
            if new_weight < c.node.weight:
                c.node.weight = new_weight
                print(f"*** Updated {c.node.label} weight ({c.node.weight}) " +
                      f"arriving from {node.label}\n")
                # optional: recreate the path taken by tracking previous node when weight is updated
                c.node.prev = node
                heappush(unvisited, (c.node.weight, c.node))

    # optional: return the route to take alongside the weight
    pathBack = []
    node = goalNode
    while node.prev is not None:
        pathBack.append(node.label)
        node = node.prev
    pathBack.append(startNode.label)

    return goalNode.weight, list(reversed(pathBack))

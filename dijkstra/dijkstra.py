from dataclasses import dataclass
from heapq import heappop, heappush
import sys

INF = sys.maxsize


@dataclass
class Node:
    label: str
    weight: int
    neighbours: list['Connection']
    prev: 'Node' = None   # optional: for tracking back to build the shortest path!

    def __lt__(self, other):
        self.weight < other.weight


@dataclass
class Connection:
    effort: int
    node: Node


def find_shortest_path(startNode, goalNode) -> tuple[int, list[str]]:
    visited = []
    seenNodes = []

    def walk(node):
        visited.append(node.label)
        print(f"*** Visited Node {node.label} from {
            node.prev.label if node.prev is not None else "unknown"} weight = {node.weight}\n")

        if node == goalNode:
            print("*** Visited goal node. Ending.")
            return

        for c in node.neighbours:
            if c.node.label in visited:
                print(f"*** Skipping weight check of {c.node.label} as it is visited already")
                continue
            new_weight = c.effort + node.weight
            if new_weight < c.node.weight:
                c.node.weight = new_weight
                print(f"*** Updated {c.node.label} weight ({c.node.weight}) " +
                      f"arriving from {node.label}\n")
                # optional: recreate the path taken by tracking previous node when weight is updated
                c.node.prev = node
                heappush(seenNodes, (c.node.weight, c.node))
            else:
                print(f"*** Not updating node weight: {c.node.label} weight = {c.node.weight}\n")

        nextNode = heappop(seenNodes)[1]
        walk(nextNode)

    walk(startNode)

    # optional: return the route to take alongside the weight
    pathBack = []
    node = goalNode
    while node.prev is not None:
        pathBack.append(node.label)
        node = node.prev
    pathBack.append(startNode.label)

    return goalNode.weight, list(reversed(pathBack))

from dataclasses import dataclass
import sys

INF = sys.maxsize


@dataclass
class Node:
    label: str
    weight: int
    neighbours: list['Connection']
    prev: 'Node' = None   # optional: for tracking back to build the shortest path!


@dataclass
class Connection:
    effort: int
    node: Node


def find_shortest_path(startNode, goalNode) -> tuple[int, list[str]]:
    visited = []

    def walk(node):
        visited.append(node)
        print(f"*** Visited Node {node.label} weight = {node.weight}\n")

        for c in node.neighbours:
            if c in visited:
                print(f"*** Skipping weight check of {c.node.label} as it is visited already")
                continue
            new_weight = c.effort + node.weight
            if new_weight < c.node.weight:
                c.node.weight = new_weight
                print(f"*** Updated {c.node.label} weight ({c.node.weight}) " +
                      f"arriving from {node.label}\n")
                # optional: recreate the path taken by tracking previous node when weight is updated
                c.node.prev = node
            else:
                print(f"*** Not updating node weight: {c.node.label} weight = {c.node.weight}\n")

        for c in sorted(node.neighbours, key=lambda c: c.node.weight):
            if c.node not in visited:
                walk(c.node)

    walk(startNode)

    # optional: return the route alongside the weight
    pathBack = []
    node = goalNode
    while node.prev is not None:
        pathBack.append(node.label)
        node = node.prev
    pathBack.append(startNode.label)

    return goalNode.weight, list(reversed(pathBack))

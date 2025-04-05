from dataclasses import dataclass
import sys

INF = sys.maxsize


@dataclass
class Node:
    label: str
    weight: int
    neighbours: list['Connection']


@dataclass
class Connection:
    effort: int
    node: Node


# sorted() is O(n log n)

def find_shortest_path(startNode, goalNode) -> tuple[int, list[str]]:
    visited = []

    # for keeping track of the shortest way back to the start node
    path = dict({})

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

                # to recreate the path taken - the key is to keep a note of the previous node
                # that we got to this node from when we update a new weight
                path[c.node.label] = node
            else:
                print(f"*** Not updating node weight: {c.node.label} weight = {c.node.weight}\n")

        for c in sorted(node.neighbours, key=lambda c: c.node.weight):
            if c.node not in visited:
                walk(c.node)

    walk(startNode)

    node = goalNode
    pathBack = []
    while node is not None:
        pathBack.append(node.label)
        node = path.get(node.label, None)

    return goalNode.weight, list(reversed(pathBack))

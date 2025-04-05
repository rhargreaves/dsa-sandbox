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


def find_shortest_path(startNode, goalNode):
    visited = []

    def walk(node):
        visited.append(node.label)
        print(f"*** Visited Node {node.label} weight = {node.weight}\n")

        for c in node.neighbours:
            new_weight = c.effort + node.weight
            if new_weight < c.node.weight:
                c.node.weight = new_weight
                print(f"*** Node {c.node.label} weight = {c.node.weight}\n")

        for c in sorted(node.neighbours, key=lambda c: c.node.weight):
            walk(c.node)

    walk(startNode)

    path = []

    def walk2(node):
        print(f"--- Walking {node.label}\n")
        if node in path:
            return False
        path.append(node)
        if node == goalNode:
            print(f"--- At goal {node.label}\n")
            return True
        for c in sorted(node.neighbours, key=lambda c: c.node.weight):
            print(f"--- Walking connection {c.node.label}\n")
            if walk2(c.node):
                return True

    walk2(startNode)

    return [n.label for n in path]

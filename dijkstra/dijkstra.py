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
        visited.append(node)
        print(f"*** Visited Node {node.label} weight = {node.weight}\n")

        for c in node.neighbours:
            new_weight = c.effort + node.weight
            if new_weight < c.node.weight:
                c.node.weight = new_weight
                print(f"*** Node {c.node.label} weight = {c.node.weight}\n")
            else:
                print(f"*** Not updating node weight: {c.node.label} weight = {c.node.weight}\n")

        for c in sorted(node.neighbours, key=lambda c: c.node.weight):
            walk(c.node)

    walk(startNode)

    path = sorted(visited, key=lambda n: n.weight)
    result = []
    for n in path:
        print(f"--- Node: {n}\n")
        result.append(n)
        if n == goalNode:
            break
    return [n.label for n in result]

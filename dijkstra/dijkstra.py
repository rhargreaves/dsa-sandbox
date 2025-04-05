from dataclasses import dataclass


@dataclass
class Node:
    label: str
    weight: int
    neighbours: list['Node']


def find_shortest_path(node):
    visited = []

    def walk(nodes):
        first_node = nodes[0]
        visited.append(first_node.label)
        if first_node.neighbours is None:
            return
        walk(first_node.neighbours)

    walk([node])

    return visited

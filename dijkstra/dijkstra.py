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

    seenNodes = []

    def get_lowest_weight_node_seen():
        nodes = list(sorted(seenNodes, key=lambda n: n.weight))
        if len(nodes) == 0:
            return None
        return nodes[0]

    def walk(node):
        visited.append(node.label)
        print(f"*** Visited Node {node.label} from {
            node.prev.label if node.prev is not None else "unknown"} weight = {node.weight}\n")

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
                if c.node not in seenNodes:
                    seenNodes.append(c.node)
            else:
                print(f"*** Not updating node weight: {c.node.label} weight = {c.node.weight}\n")

        nextNode = get_lowest_weight_node_seen()
        if nextNode is None:
            return
        seenNodes.remove(nextNode)
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

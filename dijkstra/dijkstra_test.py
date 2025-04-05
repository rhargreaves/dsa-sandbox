
from dijkstra import find_shortest_path, Node


def test_single_node():
    node = Node('S', 0, None)

    path = find_shortest_path(node)
    assert path == ['S']


def test_two_nodes():
    nodes = Node('START', 0, [
        Node('GOAL', 2, None)])

    path = find_shortest_path(nodes)
    assert path == ['START', 'GOAL']


def test_three_nodes_one_path():
    nodes = Node('START', 0, [
        Node('A', 2, [
            Node('GOAL', 2, None)])])

    path = find_shortest_path(nodes)
    assert path == ['START', 'A', 'GOAL']


from dijkstra import find_shortest_path


def test_single_node():
    nodes = ('S', 0, None)

    path = find_shortest_path(nodes)
    assert path == ['S']


def test_two_nodes():
    nodes = ('START', 0, [
        ('GOAL', 2, None)])

    path = find_shortest_path(nodes)
    assert path == ['START', 'GOAL']

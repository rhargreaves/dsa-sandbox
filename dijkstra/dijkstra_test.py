
from dijkstra import find_shortest_path


def test_single_node():
    nodes = ('S', 0, None)

    path = find_shortest_path(nodes)
    assert path == ['S']



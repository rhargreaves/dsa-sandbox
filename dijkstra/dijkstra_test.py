
from dijkstra import find_shortest_path, Node, Connection, INF


def test_single_node():
    node = Node('S', 0, [])

    path = find_shortest_path(node, node)
    assert path == ['S']


def test_two_nodes():
    goal = Node('GOAL', INF, [])
    node = Node('START', 0, [
        Connection(1, goal)])

    path = find_shortest_path(node, goal)
    assert path == ['START', 'GOAL']


def test_three_nodes_one_path():
    goal = Node('GOAL', INF, [])
    node = Node('START', 0, [
       Connection(1, Node('A', INF, [
            Connection(1, goal)]))])

    path = find_shortest_path(node, goal)
    assert path == ['START', 'A', 'GOAL']


def test_four_nodes_diamond():
    goal = Node('GOAL', INF, [])
    node = Node('START', 0, [
        Connection(3, Node('A', INF, [Connection(1, goal)])),
        Connection(2, Node('B', INF, [Connection(1, goal)]))
        ])

    path = find_shortest_path(node, goal)
    assert path == ['START', 'B', 'GOAL']

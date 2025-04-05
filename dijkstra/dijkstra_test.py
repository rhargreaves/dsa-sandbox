
from dijkstra import find_shortest_path, Node, Connection, INF


def test_single_node():
    node = Node('S', 0, [])

    distance, path = find_shortest_path(node, node)

    assert distance == 0
    assert path == ['S']


def test_two_nodes():
    goal = Node('GOAL', INF, [])
    node = Node('START', 0, [
        Connection(1, goal)])

    distance, path = find_shortest_path(node, goal)

    assert distance == 1
    assert path == ['START', 'GOAL']


def test_three_nodes_one_path():
    goal = Node('GOAL', INF, [])
    node = Node('START', 0, [
       Connection(1, Node('A', INF, [
            Connection(1, goal)]))])

    distance, path = find_shortest_path(node, goal)

    assert distance == 2
    assert path == ['START', 'A', 'GOAL']


def test_four_nodes_diamond():
    goal = Node('GOAL', INF, [])
    node = Node('START', 0, [
        Connection(3, Node('A', INF, [Connection(1, goal)])),
        Connection(2, Node('B', INF, [Connection(1, goal)]))
        ])

    distance, path = find_shortest_path(node, goal)

    assert distance == 3
    assert path == ['START', 'B', 'GOAL']


def test_four_nodes_diamond_2():
    goal = Node('GOAL', INF, [])
    node = Node('START', 0, [
        Connection(1, Node('A', INF, [Connection(1, goal)])),
        Connection(2, Node('B', INF, [Connection(1, goal)]))
        ])

    distance, path = find_shortest_path(node, goal)

    assert distance == 2
    assert path == ['START', 'A', 'GOAL']


def test_complex_graph():
    goal = Node('GOAL', INF, [])

    g_node = Node('G', INF, [Connection(7, goal)])
    h_node = Node('H', INF, [Connection(5, goal)])

    c_node = Node('C', INF, [Connection(3, g_node)])
    d_node = Node('D', INF, [Connection(6, g_node)])

    e_node = Node('E', INF, [Connection(1, h_node)])
    f_node = Node('F', INF, [Connection(5, h_node)])

    a_node = Node('A', INF, [Connection(2, c_node), Connection(2, d_node)])
    b_node = Node('B', INF, [Connection(3, e_node), Connection(12, f_node)])

    start_node = Node('START', 0, [Connection(1, a_node), Connection(2, b_node)])

    distance, path = find_shortest_path(start_node, goal)

    assert distance == 11
    assert path == ['START', 'B', 'E', 'H', 'GOAL']

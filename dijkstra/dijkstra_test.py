
from dijkstra import find_shortest_path, Node, Edge, INF


def test_single_node():
    node = Node('S', 0, [])

    weight, path = find_shortest_path(node, node)

    assert weight == 0
    assert path == ['S']


def test_two_nodes():
    goal = Node('GOAL', INF, [])
    node = Node('START', 0, [
        Edge(1, goal)])

    weight, path = find_shortest_path(node, goal)

    assert weight == 1
    assert path == ['START', 'GOAL']


def test_three_nodes_one_path():
    goal = Node('GOAL', INF, [])
    node = Node('START', 0, [
       Edge(1, Node('A', INF, [
            Edge(1, goal)]))])

    weight, path = find_shortest_path(node, goal)

    assert weight == 2
    assert path == ['START', 'A', 'GOAL']


def test_four_nodes_diamond():
    goal = Node('GOAL', INF, [])
    node = Node('START', 0, [
        Edge(3, Node('A', INF, [Edge(1, goal)])),
        Edge(2, Node('B', INF, [Edge(1, goal)]))
        ])

    weight, path = find_shortest_path(node, goal)

    assert weight == 3
    assert path == ['START', 'B', 'GOAL']


def test_four_nodes_diamond_2():
    goal = Node('GOAL', INF, [])
    node = Node('START', 0, [
        Edge(1, Node('A', INF, [Edge(1, goal)])),
        Edge(2, Node('B', INF, [Edge(1, goal)]))
        ])

    weight, path = find_shortest_path(node, goal)

    assert weight == 2
    assert path == ['START', 'A', 'GOAL']


def test_complex_graph():
    goal = Node('GOAL', INF, [])

    g_node = Node('G', INF, [Edge(7, goal)])
    h_node = Node('H', INF, [Edge(5, goal)])

    c_node = Node('C', INF, [Edge(3, g_node)])
    d_node = Node('D', INF, [Edge(6, g_node)])

    e_node = Node('E', INF, [Edge(1, h_node)])
    f_node = Node('F', INF, [Edge(5, h_node)])

    a_node = Node('A', INF, [Edge(2, c_node), Edge(2, d_node)])
    b_node = Node('B', INF, [Edge(3, e_node), Edge(12, f_node)])

    start_node = Node('START', 0, [Edge(1, a_node), Edge(2, b_node)])

    weight, path = find_shortest_path(start_node, goal)

    assert weight == 11
    assert path == ['START', 'B', 'E', 'H', 'GOAL']

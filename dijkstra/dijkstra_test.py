
from dijkstra import find_shortest_path, Node, Edge, INF


def connect_nodes(node1, node2, weight):
    node1.neighbours.append(Edge(weight, node2))
    node2.neighbours.append(Edge(weight, node1))


def test_single_node():
    node = Node('S', 0)

    weight, path = find_shortest_path(node, node)

    assert weight == 0
    assert path == ['S']


def test_two_nodes():
    goal = Node('GOAL')
    node = Node('START', 0, [
        Edge(1, goal)])

    weight, path = find_shortest_path(node, goal)

    assert weight == 1
    assert path == ['START', 'GOAL']


def test_three_nodes_one_path():
    goal = Node('GOAL')
    node = Node('START', 0, [
        Edge(1, Node('A', neighbours=[
            Edge(1, goal)]))])

    weight, path = find_shortest_path(node, goal)

    assert weight == 2
    assert path == ['START', 'A', 'GOAL']


def test_four_nodes_diamond():
    goal = Node('GOAL')
    node = Node('START', 0, [
        Edge(3, Node('A', INF, [Edge(1, goal)])),
        Edge(2, Node('B', INF, [Edge(1, goal)]))
    ])

    weight, path = find_shortest_path(node, goal)

    assert weight == 3
    assert path == ['START', 'B', 'GOAL']


def test_four_nodes_diamond_2():
    goal = Node('GOAL')
    node = Node('START', 0, [
        Edge(1, Node('A', INF, [Edge(1, goal)])),
        Edge(2, Node('B', INF, [Edge(1, goal)]))
    ])

    weight, path = find_shortest_path(node, goal)

    assert weight == 2
    assert path == ['START', 'A', 'GOAL']


def test_complex_graph():
    goal = Node('GOAL')

    g_node = Node('G', neighbours=[Edge(7, goal)])
    h_node = Node('H', neighbours=[Edge(5, goal)])

    c_node = Node('C', neighbours=[Edge(3, g_node)])
    d_node = Node('D', neighbours=[Edge(6, g_node)])

    e_node = Node('E', neighbours=[Edge(1, h_node)])
    f_node = Node('F', neighbours=[Edge(5, h_node)])

    a_node = Node('A', neighbours=[Edge(2, c_node), Edge(2, d_node)])
    b_node = Node('B', neighbours=[Edge(3, e_node), Edge(12, f_node)])

    start_node = Node('START', 0, [Edge(1, a_node), Edge(2, b_node)])

    weight, path = find_shortest_path(start_node, goal)

    assert weight == 11
    assert path == ['START', 'B', 'E', 'H', 'GOAL']


def test_complex_graph_with_cheeky_shortcut():
    goal = Node('GOAL')

    g_node = Node('G', neighbours=[Edge(7, goal)])
    h_node = Node('H', neighbours=[Edge(5, goal)])

    c_node = Node('C', neighbours=[Edge(3, g_node)])
    d_node = Node('D', neighbours=[Edge(6, g_node)])
    e_node = Node('E', neighbours=[Edge(1, h_node)])
    f_node = Node('F', neighbours=[Edge(5, h_node)])

    connect_nodes(d_node, e_node, 1)

    a_node = Node('A', neighbours=[Edge(2, c_node), Edge(2, d_node)])
    b_node = Node('B', neighbours=[Edge(3, e_node), Edge(12, f_node)])

    start_node = Node('START', 0, [Edge(1, a_node), Edge(2, b_node)])

    weight, path = find_shortest_path(start_node, goal)

    assert weight == 10
    assert path == ['START', 'A', 'D', 'E', 'H', 'GOAL']


def test_another_complex_graph_with_nodes_with_more_than_2_edges():
    goal = Node('GOAL')
    a_node = Node('A', 0)
    b_node = Node('B')
    c_node = Node('C')
    d_node = Node('D')
    e_node = Node('E')
    g_node = Node('G')

    connect_nodes(a_node, b_node, 4)
    connect_nodes(a_node, c_node, 3)
    connect_nodes(a_node, e_node, 7)

    connect_nodes(b_node, c_node, 6)
    connect_nodes(b_node, d_node, 5)

    connect_nodes(c_node, d_node, 11)
    connect_nodes(c_node, e_node, 8)

    connect_nodes(d_node, e_node, 2)
    connect_nodes(d_node, g_node, 10)
    connect_nodes(d_node, goal, 2)

    connect_nodes(e_node, g_node, 5)
    connect_nodes(g_node, goal, 3)

    weight, path = find_shortest_path(a_node, goal)

    assert weight == 11
    assert path == ['A', 'B', 'D', 'GOAL']

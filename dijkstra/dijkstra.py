
def find_shortest_path(node):
    visited = []

    def walk(nodes):
        first_node = nodes[0]
        visited.append(first_node[0])
        if first_node[2] is None:
            return
        walk(first_node[2])

    walk([node])

    return visited

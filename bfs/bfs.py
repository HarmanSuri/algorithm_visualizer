from graph.graph_visualizer import visit_node, initialize_graph, close_window


def bfs(graph: list[list[int]]) -> tuple:
    num_vertex = len(graph)

    visited = [False] * num_vertex
    parents = [None] * num_vertex
    queue = [0]
    visited[0] = True
    visit_node(centres, 0, parents, win)

    while queue != []:
        v = queue.pop(0)
        for n in graph[v]:
            if not visited[n]:
                visited[n] = True
                parents[n] = v
                queue.append(n)
                visit_node(centres, n, parents, win)

    return parents


if __name__ == '__main__':
    graph = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

    centres, win = initialize_graph(graph, 1000, 600)

    bfs(graph)

    close_window(win)

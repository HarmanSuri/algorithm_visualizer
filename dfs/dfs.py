from graph.graph_visualizer import visit_node, initialize_graph, close_window


def dfs(graph: list[list[int]]) -> tuple:
    num_vertex = len(graph)

    visited = [False] * num_vertex
    parents = [None] * num_vertex

    for v in range(num_vertex):
        if not visited[v]:
            dfs_visit(graph, v, visited, parents)

    return parents


def dfs_visit(graph: list[list[int]], vertex: int, visited: list[bool], parents: list[int]) -> None:
    visited[vertex] = True

    visit_node(centres, vertex, parents, win)

    for neigbour in graph[vertex]:
        if not visited[neigbour]:
            parents[neigbour] = vertex
            dfs_visit(graph, neigbour, visited, parents)


if __name__ == '__main__':
    graph = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

    centres, win = initialize_graph(graph, 1000, 600)

    dfs(graph)

    close_window(win)

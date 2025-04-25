
def dfs(graph: list[list[int]]) -> tuple:
    num_vertex = len(graph)

    visited = [False] * num_vertex
    parents = [None] * num_vertex

    for v in range(num_vertex):
        if not visited[v]:
            dfs_visit(graph, v, visited, parents)

    return parents


def dfs_visit(graph: list[list[int]], vertex: int, visited: list, parent: list) -> None:
    visited[vertex] = True

    for neigbour in graph[vertex]:
        if not visited[neigbour]:
            parent[neigbour] = vertex
            dfs_visit(graph, neigbour, visited, parent)


if __name__ == '__main__':
    graph = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

    print(dfs(graph))

from graphics import *
from math import pi, sin, cos, sqrt
from time import sleep

NODE_DISTANCE = 200
NODE_RADIUS = 30


def draw_vertices(graph: list[list[int]], win: GraphWin) -> list[tuple[float, float]]:
    num_vertex = len(graph)
    angle = 360 / num_vertex
    # convert angle to radians
    angle = angle * (pi / 180)

    centre = (win.getWidth() / 2, win.getHeight() / 2)
    vertex_centres = []

    for v in range(num_vertex):
        x = centre[0] + NODE_DISTANCE * cos(angle * v)
        y = centre[1] + NODE_DISTANCE * sin(angle * v)
        vertex_centres.append((x, y))

        node = Circle(Point(x, y), NODE_RADIUS)
        node.draw(win)
        num = Text(Point(x, y), f'{v}')
        num.draw(win)

    return vertex_centres


def _get_unit_vector(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    vector = (point2[0] - point1[0],
              point2[1] - point1[1])

    vector_norm = sqrt(vector[0] ** 2 + vector[1] ** 2)
    return (vector[0] / vector_norm, vector[1] / vector_norm)


def draw_edges(graph: list[list[int]], centres: list[tuple[float, float]], win: GraphWin) -> None:
    num_vertex = len(graph)

    for v in range(num_vertex):
        v_centre = centres[v]
        for n in graph[v]:
            n_centre = centres[n]

            unit_vector = _get_unit_vector(v_centre, n_centre)

            edge = Line(Point(v_centre[0] + NODE_RADIUS * unit_vector[0], v_centre[1] + NODE_RADIUS * unit_vector[1]),
                        Point(n_centre[0] - NODE_RADIUS * unit_vector[0], n_centre[1] - NODE_RADIUS * unit_vector[1]))
            edge.draw(win)


def visit_node(centres: list[tuple[float, float]], vertex: int, parents: list[int], win: GraphWin) -> None:
    v_centre = centres[vertex]

    if parents[vertex] is not None:
        n_centre = centres[parents[vertex]]

        unit_vector = _get_unit_vector(v_centre, n_centre)

        edge = Line(Point(v_centre[0] + NODE_RADIUS * unit_vector[0], v_centre[1] + NODE_RADIUS * unit_vector[1]),
                    Point(n_centre[0] - NODE_RADIUS * unit_vector[0], n_centre[1] - NODE_RADIUS * unit_vector[1]))
        edge.setOutline('red')

        sleep(1)

        edge.draw(win)

    node = Circle(Point(centres[vertex][0], centres[vertex][1]), NODE_RADIUS)
    node.setOutline('red')

    sleep(0.5)

    node.draw(win)


def initialize_graph(graph: GraphWin, win_width: float, win_height: float) -> tuple:
    win = GraphWin("My Circle", win_width, win_height)

    centres = draw_vertices(graph, win)
    draw_edges(graph, centres, win)

    num = Text(Point(win_width / 2, win_height * .9),
               'Click a key to exit when search is done')
    num.draw(win)

    return centres, win


def close_window(window: GraphWin) -> None:
    window.getKey()  # pause for click in window
    window.close()


def _main():
    win = GraphWin("My Circle", 1000, 600)

    centres = draw_vertices(graph, win)
    draw_edges(graph, centres, win)

    win.getKey()  # pause for click in window

    win.close()


if __name__ == '__main__':
    graph = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2], [], []]
    _main()

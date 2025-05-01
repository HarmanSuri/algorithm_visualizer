from math import atan2, sqrt
from random import randint, choice, shuffle


def get_convex_polygon(num_vertex):
    # Generate two lists of random X and Y coordinates
    x_vals = sorted([randint(50, 950) for _ in range(num_vertex)])
    y_vals = sorted([randint(50, 550) for _ in range(num_vertex)])

    # Isolate the extreme points
    x_min = x_vals[0]
    x_max = x_vals[-1]
    y_min = y_vals[0]
    y_max = y_vals[-1]

    x_vec = []
    y_vec = []

    last_top = x_min
    last_bot = x_min

    last_left = y_min
    last_right = y_min

    # Divide the interior points into two chains & Extract the vector components
    for i in range(1, num_vertex - 1):
        x = x_vals[i]
        y = y_vals[i]

        if choice([True, False]) == 1:
            x_vec.append(x - last_top)
            last_top = x
        else:
            x_vec.append(last_bot - x)
            last_bot = x

        if choice([True, False]) == 1:
            y_vec.append(y - last_left)
            last_left = y
        else:
            y_vec.append(last_right - y)
            last_right = y

    x_vec.append(x_max - last_top)
    x_vec.append(last_bot - x_max)

    y_vec.append(y_max - last_left)
    y_vec.append(last_right - y_max)

    # Randomly pair up the X- and Y-components
    shuffle(y_vec)

    # Combine the paired up components into vectors
    # Sort the vectors by angle
    vec = sorted([(x, y) for x, y in zip(x_vec, y_vec)],
                 key=lambda v: atan2(v[1], v[0]))

    # Lay them end-to-end
    x, y = 0, 0
    min_polygon_x = 0
    min_polygon_y = 0
    points = []

    for i in range(num_vertex):
        points.append((x, y))

        x += vec[i][0]
        y += vec[i][1]

        min_polygon_x = min(min_polygon_x, x)
        min_polygon_y = min(min_polygon_y, y)

    # Move the polygon to the original min and max coordinates
    x_shift = x_min - min_polygon_x
    y_shift = y_min - min_polygon_y

    for i in range(num_vertex):
        p = points[i]
        points[i] = (p[0] + x_shift, p[1] + y_shift)

    return points


def triangle_perimeter(points):
    perimeter = 0

    for i in range(-1, len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        perimeter += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return perimeter


def possible_optimal_chords(i, j, points, subproblems):
    possible_chords = []

    for k in range(i + 1, j):
        chord = triangle_perimeter(
            [points[i], points[k], points[j]]) + subproblems[i][k] + subproblems[k][j]
        possible_chords.append(chord)

    return possible_chords


def min_cost_polygon_triangulation(points):
    n = len(points)
    polygon_subproblems = [[0] * n for _ in range(n)]

    for i in range(0, n - 2):
        polygon_subproblems[i][i + 2] = triangle_perimeter(
            points[i: i + 3])

    for c in range(3, n):
        for i in range(0, n - c):
            j = i + c
            polygon_subproblems[i][j] = min(
                possible_optimal_chords(i, j, points, polygon_subproblems))

    return polygon_subproblems[0][n - 1]


if __name__ == '__main__':
    p = get_convex_polygon(5)

    print(min_cost_polygon_triangulation(p))

    print(min_cost_polygon_triangulation(
        [(0, 2), (1, 2), (2, 1), (1, 0), (0, 0)]))

from heapq import heappush, heappop
from heuristica import manhattan_distance
from movimentos import valid_moves

def a_star(x0, y0, xf, yf, N):
    open_list = [(0, (x0, y0))]
    closed_set = set()
    g_score = {(x0, y0): 0}
    f_score = {(x0, y0): manhattan_distance(x0, y0, xf, yf)}
    came_from = {}

    while open_list:
        current_f, (current_x, current_y) = heappop(open_list)

        if current_x == xf and current_y == yf:
            return reconstruct_path((xf, yf), came_from)

        closed_set.add((current_x, current_y))

        for move in valid_moves(current_x, current_y, N):
            next_x, next_y = move
            tentative_g_score = g_score[(current_x, current_y)] + 1

            if (next_x, next_y) in closed_set and tentative_g_score >= g_score.get((next_x, next_y), float('inf')):
                continue

            if tentative_g_score < g_score.get((next_x, next_y), float('inf')):
                came_from[(next_x, next_y)] = (current_x, current_y)
                g_score[(next_x, next_y)] = tentative_g_score
                f_score[(next_x, next_y)] = tentative_g_score + manhattan_distance(next_x, next_y, xf, yf)
                heappush(open_list, (f_score[(next_x, next_y)], (next_x, next_y)))

    return None

def reconstruct_path(current, came_from):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

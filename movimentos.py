def valid_moves(x, y, N):
    moves = []
    possible_moves = [(x + 1, y + 2), (x + 2, y + 1), (x + 2, y - 1), (x + 1, y - 2),
                     (x - 1, y - 2), (x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2)]

    for move in possible_moves:
        if 0 <= move[0] < N and 0 <= move[1] < N:
            moves.append(move)
    return moves
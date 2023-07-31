import random

def is_safe_queens(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
    return True

def generate_queens():
    safe_positions = []
    while len(safe_positions) < 4:
        positions = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]
        if is_safe_queens(positions):
            safe_positions.append(positions)
    return safe_positions

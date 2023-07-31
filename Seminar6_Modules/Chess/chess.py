from tqdm import tqdm
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
    for _ in tqdm(range(100000)):  # 100000 здесь - это примерное количество попыток, которое вы хотите сделать
        positions = [(i+1, random.randint(1, 8)) for i in range(8)]  # каждый ферзь в отдельной строке
        if is_safe_queens(positions):
            safe_positions.append(positions)
            if len(safe_positions) >= 4:
                break
    return safe_positions

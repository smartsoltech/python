def sum_between_indices(numbers, idx1, idx2):
    start, end = sorted([idx1, idx2])
    start = max(0, start)
    end = min(len(numbers), end)
    return sum(numbers[start:end+1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
idx1 = 3
idx2 = 22

print(sum_between_indices(numbers, idx1, idx2))

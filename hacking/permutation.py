def print_combinations(x, y, z, n):
  combinations = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
  print(combinations)

print_combinations(1, 1, 1, 2)
print_combinations(1, 1, 2, 3)
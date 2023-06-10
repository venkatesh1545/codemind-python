def print_pattern(n):
    size = n * 2 - 1
    pattern = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            pattern[i][j] = n - min(i, j, size - i - 1, size - j - 1)
    for i in range(size):
        for j in range(size):
            print(pattern[i][j], end=" ")
        print()
n=int(input())
print_pattern(n)

def print_pattern(n):
    for i in range(1, n+1):
        if i == n or i == 1:
            print('*' * i)
        else:
            print('*' + ' ' * (i-2) + '*')
n=int(input())
print_pattern(n)

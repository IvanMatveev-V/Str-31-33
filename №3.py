n = int(input())

N = 1

for i in range(1, n+1):
    N *= 2
    print(f"Через {3 * i} будет амеб: {N}")
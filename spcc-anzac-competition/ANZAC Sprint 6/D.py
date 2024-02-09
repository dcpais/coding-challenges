import math

[h, w] = [int(x) for x in input().split()]

grid = []

for y in range(h):
    line = input()
    cs = [c for c in line]
    s = []
    for c in cs:
        s.append(c)
    s.append('#')
    grid.append(s)

s = []
for _ in range(w):
    s.append('#')
grid.append(s)

print(grid)

best = 0

dp = [[[-1, -1] for _ in range(w+1)] for _ in range(h+1)]

for x in range(w+1):
    dp[h][x][0] = 0
    dp[h][x][1] = 0

for y in range(h+1):
    dp[y][w][0] = 0
    dp[y][w][1] = 0

dp[h-1][w-1][0] = 0
dp[h-1][w-1][1] = 0

for y in range(h-1, -1, -1):
    for x in range(w-1, -1, -1):
        circle = 0
        if grid[y][x] == 'O':
            circle = 1
        # top
        dp[y][x][0] = max(dp[y][x+1][0], dp[y+1][x][1] + circle)
        # left
        dp[y][x][1] = max(dp[y+1][x][0] + circle, dp[y+1][x][1])

n = max(dp[0][0][0], dp[0][0][1])

# print(10*h + 10*w - n * (2.5 * math.pi - 10))
print(n)
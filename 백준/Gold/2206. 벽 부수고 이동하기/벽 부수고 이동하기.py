import sys

n, m = map(int, input().split())
maze = []
wall = [[False] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited_before_chance = [[False] * m for _ in range(n)]
for i in range(n):
    maze.append(list(map(int, list(str(sys.stdin.readline().strip())))))
    for j in range(m):
        if maze[i][j]:
            visited[i][j] = True
            wall[i][j] = True
goto = set()
goto_before_chance = {(0, 0)}
count = 1
while (n - 1, m - 1) not in goto and (n - 1, m - 1) not in goto_before_chance:
    if not goto and not goto_before_chance:
        count = -1
        break
    for x, y in goto:
        visited[x][y] = True
    for x, y in goto_before_chance:
        visited_before_chance[x][y] = True
        visited[x][y] = True
    new_goto = set()
    new_goto_before_chance = set()
    for x, y in goto:
        for a, b in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
            if 0 <= a < n and 0 <= b < m and not visited[a][b]:
                new_goto.add((a, b))
    for x, y in goto_before_chance:
        for a, b in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
            if 0 <= a < n and 0 <= b < m and not visited_before_chance[a][b]:
                if not wall[a][b]:
                    new_goto_before_chance.add((a, b))
                else:
                    new_goto.add((a, b))
    goto = new_goto
    goto_before_chance = new_goto_before_chance
    count += 1
print(count)

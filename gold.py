import sys


def dfs(x, y):
    if x < 0 or y < 0 or x >= w or y >= h or visited[y][x] or grid[y][x] == '#':
        return

    visited[y][x] = True

    if trap_nearby(x, y):
        if grid[y][x] == 'G':
            global unsafe_gold
            unsafe_gold.append((x, y))
        return

    if grid[y][x] == 'G':
        global safe_gold
        safe_gold.append((x, y))

    for dx, dy in dirs:
        dfs(x + dx, y + dy)


def trap_nearby(x, y):
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx >= 0 and ny >= 0 and nx < w and ny < h and grid[ny][nx] == 'T':
            return True
    return False


dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
w, h = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(h)]
visited = [[False] * w for _ in range(h)]
safe_gold = []
unsafe_gold = []

start_x, start_y = None, None
for y in range(h):
    for x in range(w):
        if grid[y][x] == 'P':
            start_x, start_y = x, y
            break
    if start_x is not None:
        break

dfs(start_x, start_y)
gold_count = len(set(safe_gold) - set(unsafe_gold))

print(gold_count)

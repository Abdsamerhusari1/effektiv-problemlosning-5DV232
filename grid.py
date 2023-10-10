from collections import deque


def is_valid(x, y, n, m, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]


def bfs(grid, n, m):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 0)])  # x, y, depth

    while queue:
        x, y, depth = queue.popleft()

        if x == n - 1 and y == m - 1:
            return depth

        for dx, dy in directions:
            jump = grid[x][y]
            new_x, new_y = x + dx * jump, y + dy * jump
            if is_valid(new_x, new_y, n, m, visited):
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, depth + 1))

    return -1


def main():
    n, m = map(int, input().split())
    grid = [list(map(int, list(input().strip()))) for _ in range(n)]
    print(bfs(grid, n, m))


if __name__ == "__main__":
    main()

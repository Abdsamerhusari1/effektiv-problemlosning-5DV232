import sys
from collections import deque

# Create moves for Knight
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

# Initialize an empty chess board
board = [['' for _ in range(8)] for _ in range(8)]

def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def bfs(sx, sy):
    global board
    board = [['' for _ in range(8)] for _ in range(8)]
    board[sx][sy] = 0

    queue = deque()
    queue.append((sx, sy))

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if is_valid(nx, ny) and board[nx][ny] == '':
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

def solve(case):
    bfs(8 - int(case[1]), ord(case[0]) - ord('a'))

    max_distance = max(max(row) for row in board)
    hiding_places = []

    for i in range(8):
        for j in range(8):
            if board[i][j] == max_distance:
                hiding_places.append(f"{chr(j + ord('a'))}{8 - i}")

    # Custom sort: first by rank descending, then by file ascending
    hiding_places.sort(key=lambda x: (-int(x[1]), x[0]))

    return max_distance, hiding_places

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        case = input().strip()
        max_distance, hiding_places = solve(case)
        print(f"{max_distance} {' '.join(hiding_places)}")

if __name__ == "__main__":
    main()

from heapq import heappush, heappop

def adjacent_cells(M, N, position):
    x, y = position
    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= i < M and 0 <= j < N:
            yield (i, j)

def shortest_ladder(matrix, M, N):
    start = (0, 0)
    goal = (M-1, N-1)
    visited = {}
    queue = [(0, start)]  
    while queue:
        ladder_height, current = heappop(queue)
        if current == goal:
            return ladder_height
        for adj in adjacent_cells(M, N, current):
            new_ladder = max(ladder_height, max(0, matrix[adj[0]][adj[1]] - matrix[current[0]][current[1]]))
            if adj not in visited or visited[adj] > new_ladder:
                visited[adj] = new_ladder
                heappush(queue, (new_ladder, adj))
    return -1

def main():
    M, N = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(M)]
    print(shortest_ladder(matrix, M, N))

if __name__ == "__main__":
    main()

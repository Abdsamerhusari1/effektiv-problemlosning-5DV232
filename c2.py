import sys
import heapq

def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    army_size = [0] + [int(sys.stdin.readline()) for _ in range(n)]
    total_army = army_size[1]
    army_size[1] = 0
    heap = []
    visited = [False] * (n+1)
    visited[1] = True
    for u in graph[1]:
        heapq.heappush(heap, (army_size[u], u))
    while heap:
        cur_army, u = heapq.heappop(heap)
        if cur_army > total_army or visited[u]:
            continue
        total_army += cur_army
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (army_size[v], v))
    print(total_army)

if __name__ == '__main__':
    main()

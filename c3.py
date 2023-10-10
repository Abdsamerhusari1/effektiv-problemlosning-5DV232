import sys
import heapq

def main():
    n, m = map(int, sys.stdin.readline().split())
    adj = [set() for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
    army_size = [0] + [int(sys.stdin.readline()) for _ in range(n)]
    visited = [False] * (n+1)
    q = []
    for u in adj[1]:
        heapq.heappush(q, (army_size[u], u))  # Min heap
    visited[1] = True
    total_army = army_size[1]
    while q:
        size, u = heapq.heappop(q)
        if visited[u] or size >= total_army:
            continue
        visited[u] = True
        total_army += size
        for v in adj[u]:
            if not visited[v]:
                heapq.heappush(q, (army_size[v], v))
    print(total_army)

if __name__ == '__main__':
    main()

import heapq

def max_army_size(n, m, bridges, army_sizes):
    graph = {i: [] for i in range(1, n+1)}
    for u, v in bridges:
        graph[u].append(v)
        graph[v].append(u)

    army_sizes = [0] + army_sizes
    current_army = army_sizes[1]

    visited = set([1])
    reachable = graph[1]
    army_list = [(army_sizes[i], i) for i in reachable]
    heapq.heapify(army_list)

    while army_list:
        min_army, min_army_island = heapq.heappop(army_list)

        if min_army < current_army:
            current_army += min_army
            visited.add(min_army_island)
            for i in graph[min_army_island]:
                if i not in visited:
                    heapq.heappush(army_list, (army_sizes[i], i))

    return current_army

if __name__ == "__main__":
    n, m = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(m)]
    army_sizes = [int(input()) for _ in range(n)]
    print(max_army_size(n, m, bridges, army_sizes))
# Sample Input 1
n, m = 6, 5
bridges = [(1, 4), (3, 4), (2, 4), (6, 3), (5, 4)]
army_sizes = [2, 4, 1, 0, 10, 2]
print(max_army_size(n, m, bridges, army_sizes))  # Expected Output: 9

# Sample Input 2
n, m = 6, 5
bridges = [(3, 4), (3, 1), (2, 3), (6, 1), (5, 3)]
army_sizes = [2, 3, 0, 1, 3, 3]
print(max_army_size(n, m, bridges, army_sizes))  # Expected Output: 3

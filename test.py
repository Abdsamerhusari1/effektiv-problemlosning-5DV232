class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]


def max_army_size(n, m, bridges, army_sizes):
    uf = UnionFind(n)
    max_army = max(army_sizes)

    for u, v in bridges:
        uf.union(u - 1, v - 1)

    component_sizes = [0] * n
    for i in range(n):
        root = uf.find(i)
        component_sizes[root] += army_sizes[i]

    return min(max(component_sizes), max_army)


n, m = 6, 5
bridges = [(1, 4), (3, 4), (2, 4), (6, 3), (5, 4)]
army_sizes = [2, 4, 1, 0, 10, 2]
print(max_army_size(n, m, bridges, army_sizes))  # Expected Output: 9

# Sample Input 2
n, m = 6, 5
bridges = [(3, 4), (3, 1), (2, 3), (6, 1), (5, 3)]
army_sizes = [2, 3, 0, 1, 3, 3]
print(max_army_size(n, m, bridges, army_sizes))  # Expected Output: 3

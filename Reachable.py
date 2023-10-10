def dfs(node, visited, city_map):
    if node in visited:
        return
    visited.add(node)
    for neighbor in city_map[node]:
        dfs(neighbor, visited, city_map)


def number_of_disconnected_components(m, roads):
    city_map = {i: [] for i in range(m)}
    for u, v in roads:
        city_map[u].append(v)
        city_map[v].append(u)

    visited = set()
    components = 0

    for node in city_map:
        if node not in visited:
            dfs(node, visited, city_map)
            components += 1

    return components


def main():
    t = int(input())
    results = []

    for _ in range(t):
        m = int(input())
        r = int(input())
        roads = [tuple(map(int, input().split())) for _ in range(r)]
        components = number_of_disconnected_components(m, roads)
        results.append(components - 1)

    for res in results:
        print(res)


if __name__ == "__main__":
    main()

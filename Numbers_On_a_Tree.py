def get_label(height, path):
    if len(path) > height:
        return None

    node = 1
    for direction in path:
        if direction == 'L':
            node = 2 * node
        elif direction == 'R':
            node = 2 * node + 1
        else:
            return None

    total_nodes = 2 ** (height + 1) - 1
    if node > total_nodes:
        return None

    return total_nodes - node + 1

# Example usage:
data = input().split()
tree_height = int(data[0])
path = data[1] if len(data) > 1 else ''
label = get_label(tree_height, path)
print(label)

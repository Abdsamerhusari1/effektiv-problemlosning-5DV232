def can_park(grid, i, j):
    if i + 1 >= len(grid) or j + 1 >= len(grid[0]):
        return False

    if grid[i][j] == '#' or grid[i + 1][j] == '#' or grid[i][j + 1] == '#' or grid[i + 1][j + 1] == '#':
        return False

    return True


def cars_squashed(grid, i, j):
    count = 0
    if grid[i][j] == 'X':
        count += 1
    if grid[i + 1][j] == 'X':
        count += 1
    if grid[i][j + 1] == 'X':
        count += 1
    if grid[i + 1][j + 1] == 'X':
        count += 1
    return count


def main():
    R, C = map(int, input().split())
    grid = [list(input().strip()) for _ in range(R)]

    results = [0, 0, 0, 0, 0]

    for i in range(R):
        for j in range(C):
            if can_park(grid, i, j):
                count = cars_squashed(grid, i, j)
                results[count] += 1

    for res in results:
        print(res)


if __name__ == '__main__':
    main()

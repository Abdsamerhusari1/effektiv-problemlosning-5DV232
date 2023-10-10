if __name__ == '__main__':
    num_mountains = int(input())
    mountain_heights = [int(height) for height in input().split()]

    max_height_to_right = [0] * num_mountains
    max_height_to_right[-1] = mountain_heights[-1]

    for i in range(num_mountains - 2, -1, -1):
        max_height_to_right[i] = max(max_height_to_right[i + 1], mountain_heights[i])

    highest_mountain_to_left = mountain_heights[0]
    optimal_jump = 0

    for i in range(1, num_mountains - 1):
        current_jump = max(0, min(highest_mountain_to_left, max_height_to_right[i]) - mountain_heights[i])
        highest_mountain_to_left = max(highest_mountain_to_left, mountain_heights[i])
        optimal_jump = max(optimal_jump, current_jump)

    print(optimal_jump)

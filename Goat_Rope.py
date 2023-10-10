import sys
import math


def calculate_distance(px, py, qx, qy):
    return math.sqrt((px - qx) ** 2 + (py - qy) ** 2)


def main():
    x, y, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    min_distance = float('inf')

    if x < x1:
        if y < y1:
            min_distance = calculate_distance(x, y, x1, y1)
        elif y > y2:
            min_distance = calculate_distance(x, y, x1, y2)
        else:
            min_distance = x1 - x
    elif x > x2:
        if y < y1:
            min_distance = calculate_distance(x, y, x2, y1)
        elif y > y2:
            min_distance = calculate_distance(x, y, x2, y2)
        else:
            min_distance = x - x2
    else:
        min_distance = min(abs(y - y1), abs(y - y2))

    print("{:.1f}".format(min_distance))


if __name__ == "__main__":
    main()

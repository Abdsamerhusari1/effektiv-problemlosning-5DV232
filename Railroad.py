def is_possible_to_build(X, Y):
    track_ends = 4 * X + 3 * Y
    return track_ends % 2 == 0


def main():
    X, Y = map(int, input().split())

    if is_possible_to_build(X, Y):
        print("possible")
    else:
        print("impossible")


if __name__ == "__main__":
    main()

def main():
    n = int(input().strip())

    knots_to_learn = set(map(int, input().strip().split()))

    knots_learned = set(map(int, input().strip().split()))

    missing_knot = knots_to_learn - knots_learned

    print(missing_knot.pop())

if __name__ == '__main__':
    main()

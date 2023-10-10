def is_possible(lengths):
    lengths.sort()

    for i in range(len(lengths) - 2):
        if lengths[i] + lengths[i + 1] > lengths[i + 2]:
            return 'possible'

    return 'impossible'

def main():
    n = int(input().strip())
    lengths = list(map(int, input().strip().split()))

    result = is_possible(lengths)
    print(result)

if __name__ == '__main__':
    main()

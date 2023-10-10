import sys

def solve(l, w):
    # check if it is possible to form a word
    if l*26 < w or l > w:
        return "impossible"

    result = []
    while l > 0:
        # determine the maximum weight a letter can have
        max_letter_weight = min(26, w - l + 1)
        # append the letter to the result
        result.append(chr(ord('a') + max_letter_weight - 1))
        # subtract the weight from the total weight
        w -= max_letter_weight
        # decrease the length
        l -= 1
    return ''.join(result)

def main():
    l, w = map(int, sys.stdin.readline().split())
    print(solve(l, w))

if __name__ == "__main__":
    main()

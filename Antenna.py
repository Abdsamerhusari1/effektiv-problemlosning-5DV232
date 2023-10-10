from collections import deque

def calculate_difference(n, c, measurements):
    min_deque, max_deque = deque(), deque()
    result = []

    for i in range(n):
        while min_deque and measurements[min_deque[-1]] >= measurements[i]:
            min_deque.pop()
        while max_deque and measurements[max_deque[-1]] <= measurements[i]:
            max_deque.pop()

        min_deque.append(i)
        max_deque.append(i)

        while min_deque and min_deque[0] < i - n:
            min_deque.popleft()
        while max_deque and max_deque[0] < i - n:
            max_deque.popleft()

        diff1 = measurements[i] - measurements[min_deque[0]] - c * (i - min_deque[0])
        diff2 = measurements[max_deque[0]] - measurements[i] - c * (i - max_deque[0])
        result.append(max(diff1, diff2))

    return result

if __name__ == "__main__":
    n, c = map(int, input().split())
    measurements = list(map(int, input().split()))
    results = calculate_difference(n, c, measurements)
    print(' '.join(map(str, results)))

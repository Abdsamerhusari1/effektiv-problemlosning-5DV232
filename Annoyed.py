import heapq

def max_annoyance(h, coworkers):
    q = [[a + d, a, d] for a, d in coworkers]
    heapq.heapify(q)

    for _ in range(h):
        next_annoyance, curr_annoyance, rate = heapq.heappop(q)
        curr_annoyance += rate
        next_annoyance = curr_annoyance + rate
        heapq.heappush(q, [next_annoyance, curr_annoyance, rate])

    return max(worker[1] for worker in q)

h, c = map(int, input().split())
coworkers = [tuple(map(int, input().split())) for _ in range(c)]

print(max_annoyance(h, coworkers))

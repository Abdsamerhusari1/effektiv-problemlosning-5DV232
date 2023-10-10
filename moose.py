import sys

def moose_points(L, r):
    if L == 0 and r == 0:
        return "Not a moose"
    elif L == r:
        return f"Even {2 * L}"
    else:
        return f"Odd {2 * max(L, r)}"

L, r = map(int, sys.stdin.readline().split())
print(moose_points(L, r))

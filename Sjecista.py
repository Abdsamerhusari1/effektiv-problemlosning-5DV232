import sys
from math import comb

def diagonal_intersections(n):
    return comb(n, 4)

def main():
    n = int(input())
    print(diagonal_intersections(n))

if __name__ == "__main__":
    main()

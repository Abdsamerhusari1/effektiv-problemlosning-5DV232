import math
from collections import Counter

def number_of_anagrams(word):
    total_chars = len(word)
    char_counts = Counter(word)
    denominator = 1
    for count in char_counts.values():
        denominator *= math.factorial(count)
    return math.factorial(total_chars) // denominator

def main():
    try:
        while True:
            word = input().strip()
            print(number_of_anagrams(word))
    except EOFError:
        pass

if __name__ == "__main__":
    main()

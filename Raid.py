import sys


def select_adventurer(skill_list, chosen_set):
    for i, (name, skills) in enumerate(skill_list):
        if name not in chosen_set:
            return name
    return None


def main():
    n = int(sys.stdin.readline().strip())
    adventurers = [sys.stdin.readline().strip().split() for _ in range(n)]

    # Create a list of tuples with the name and their skills, then sort by each skill
    adventurers_by_skill1 = sorted([(name, skills) for name, *skills in adventurers],
                                   key=lambda x: (-int(x[1][0]), x[0]))
    adventurers_by_skill2 = sorted([(name, skills) for name, *skills in adventurers],
                                   key=lambda x: (-int(x[1][1]), x[0]))
    adventurers_by_skill3 = sorted([(name, skills) for name, *skills in adventurers],
                                   key=lambda x: (-int(x[1][2]), x[0]))

    chosen_set = set()

    while len(chosen_set) + 3 <= n:
        a1 = select_adventurer(adventurers_by_skill1, chosen_set)
        a2 = select_adventurer(adventurers_by_skill2, chosen_set)
        a3 = select_adventurer(adventurers_by_skill3, chosen_set)

        if not all([a1, a2, a3]):
            break

        chosen_set.update([a1, a2, a3])
        print(" ".join(sorted([a1, a2, a3])))


if __name__ == "__main__":
    main()

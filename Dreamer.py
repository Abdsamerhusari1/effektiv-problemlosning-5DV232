from itertools import permutations


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def is_valid_date(day, month, year):
    if month == 2:
        if is_leap_year(year):
            return 1 <= day <= 29
        return 1 <= day <= 28
    if month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    return False


def earliest_date(digits):
    earliest = None
    count = 0
    seen_dates = set()

    for perm in permutations(digits):
        day, month, year = int(''.join(perm[:2])), int(''.join(perm[2:4])), int(''.join(perm[4:]))
        if (day, month, year) in seen_dates:
            continue
        seen_dates.add((day, month, year))

        if is_valid_date(day, month, year) and year >= 2000:
            count += 1
            if not earliest or (year, month, day) < earliest:
                earliest = (year, month, day)

    if not earliest:
        return "0"
    return f"{count} {str(earliest[2]).zfill(2)} {str(earliest[1]).zfill(2)} {earliest[0]}"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        digits = input().replace(" ", "")
        print(earliest_date(digits))

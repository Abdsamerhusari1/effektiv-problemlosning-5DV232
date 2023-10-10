K, n = map(int, input().split())
karl_entry_year, karl_strength = map(int, input().split())

year_of_victory = "unknown"
highest_strength = karl_strength

for _ in range(n + K - 2):
    entry_year, strength = map(int, input().split())

    if strength > highest_strength:
        highest_strength = strength

    if karl_strength < highest_strength:
        year_of_victory = entry_year

print(year_of_victory)

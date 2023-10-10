def missing_letters(phrase):
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    letters = set(phrase.lower())

    missing = list(alphabet_set - letters)
    missing.sort()

    return "".join(missing)


num_phrases = int(input().strip())

for _ in range(num_phrases):
    phrase = input().strip()

    missing = missing_letters(phrase)
    if missing:
        print(f'missing {missing}')
    else:
        print('pangram')



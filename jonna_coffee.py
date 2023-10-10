def max_awake_lectures(n, s):
    s = [int(x) for x in s]
    awake = 0
    coffee = 0
    potential = [] # lectures that Jonna could attend if she had coffee
    for i in range(n):
        if s[i] == 0 and coffee > 0:
            # Jonna attends the lecture and drinks a coffee
            coffee -= 1
            awake += 1
        elif s[i] == 1 and coffee == 0:
            # Jonna gets two coffee and holds it
            coffee += 2
            awake += 1
        elif s[i] == 1 and coffee == 1:
            # Jonna gets a coffee and holds it
            coffee += 1
            awake += 1
        elif s[i] == 1 and coffee == 2:
            awake += 1
    return awake

n = int(input())
s = input()
print(max_awake_lectures(n, s))

# Open and read the file
N = int(input())

# Validate the input
if 1 <= N <= 100:
    # Iterate from 1 to N
    for i in range(1, N + 1):
        print(f"{i} Abracadabra")
else:
    print("Invalid input! Enter a number between 1 and 100.")

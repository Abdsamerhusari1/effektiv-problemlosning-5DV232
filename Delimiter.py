def validate_delimiters(L, s):
    stack = []
    opening = "({["
    closing = ")}]"
    mapping = {')': '(', ']': '[', '}': '{'}

    for i, char in enumerate(s):
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or mapping[char] != stack[-1]:
                return char, i
            stack.pop()

    if not stack:
        return "ok so far"
    else:
        return "ok so far"

if __name__ == "__main__":
    L = int(input().strip())
    s = input().strip()

    result = validate_delimiters(L, s)

    if type(result) is tuple:
        print(result[0], result[1])
    else:
        print(result)

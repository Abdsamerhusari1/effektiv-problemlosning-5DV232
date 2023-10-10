

def precompute_results():
    results = {}
    operators = ['//', '*', '+', '-']
    four = '4'

    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                expression = f'{four} {op1} {four} {op2} {four} {op3} {four}'
                value = int(eval(expression))
                results[value] = expression.replace('//', '/') + ' = ' + str(value)
    return results
def main():
    # Precompute the results
    results = precompute_results()

    m = int(input())
    for _ in range(m):
        n = int(input())
        print(results.get(n, "no solution"))

if __name__ == "__main__":
    main()

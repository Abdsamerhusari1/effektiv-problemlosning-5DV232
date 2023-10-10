import sys
from decimal import getcontext, Decimal

getcontext().prec = 22

a, b, c = map(int, sys.stdin.readline().split())

result = Decimal(a) * Decimal(b) / Decimal(c)

print('{0:.18f}'.format(result))

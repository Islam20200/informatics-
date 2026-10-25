import sys

a, b = map(int, sys.stdin.read().split())

start = a if a % 2 == 0 else a + 1
print(*range(start, b + 1, 2))

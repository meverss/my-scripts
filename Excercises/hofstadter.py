from functools import lru_cache as cache
from sys import setrecursionlimit as rlimit
rlimit(10**6)

num = int(input())

@cache(10000)
def q(num):
  if num == 1 or num == 2:
    return 1
  else:
    return q(num - q(num-1)) + q(num - q(num-2))

print(q(num))

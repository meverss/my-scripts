from functools import lru_cache as cache
import sys
#sys.setrecursionlimit(10**6)

num = int(input())
#@cache(1000)
def q(num):
  if num == 1 or num == 2:
    return 1
  else:
    return q(num - q(num-1)) + q(num - q(num-2))

print(q(num))
fib.cache_info()
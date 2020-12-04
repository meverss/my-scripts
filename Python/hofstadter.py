from functools import lru_cache as cache
from sys import setrecursionlimit as rlimit
from os import system

system('clear')
rlimit(10**6)

num = int(input())
c = int((10**(len(str(num)))) / 2)
@cache(c)
def q(num):
  global tmp
  if num == 1 or num == 2:
    return 1
  else:
    return q(num - q(num-1)) + q(num - q(num-2))

Q = q(num)
hits = f'Hits: {q.cache_info()[0]}'
print(Q)
print('_' * len(hits))
print(hits)

"""
Title:	Wrong Term in Arithmetic Sequence
Author:	MeVeRsS

Description:
In mathematics, an arithmetic progression (AP) or arithmetic
sequence is a sequence of numbers such that the difference
between the consecutive terms is constant

Given an AP, find the wrong term knowing that the first one
is right.

Input:
The first line of input contains a single line T, which
represents the number of testcases.

Then first line of each test case contains an integer
N :Total number of terms.

Then N space separated integers denoting the sequence.

Sample Input:
2
5
1 3 5 6 9
4
1 2 3 5

Output:
For each test case.
Print the wrongly entered term.

Sample Output:
6
5

Contraints:
1 <= T <= 100
4 <= N <= 1000
1 <= Terms <= 1000
"""

t = int(input() or 1)
wrong = []
i=1
if 1 <= t <= 100:
  while i <= t:
    nums = int(input() or 5)
    if 4 <= nums <= 1000:
      nlist = input().split() or '1 3 5 6 9'.split()
      if 1 <= len(nlist) <= 1000:
        f = list(int(nlist[x+1])-int(nlist[x]) for x in range(len(nlist)-1))
        sec = max(filter(lambda x: f.count(x) >= 2, f))
        for n in range(len(nlist)):
          if int(nlist[n]) - int(nlist[n-1]) != sec and n != 0:
            wrong.append(nlist[n])
            break
    i += 1
for x in wrong:
  print(x)
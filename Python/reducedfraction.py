"""
Title:	Reducing a Fraction
Author:	MeVeRsS

Description:
Given a fraction, represent it in it's reduced form.

Input:
2 integers separated by space denoting the numerator
and denominator respectively.

Output:
Print the reduced form of the fraction.
"""

nums = input().split()
nums = [int(x) for x in nums]
ld = []

for i in range(2):
  ld.append(list(nums[i] / x for x in range(1,10**(len(str(max(nums) - 1)))) if nums[i] / x == int(nums[i] / x)))

mcd = max(list(filter(lambda x: float(x) in ld[1], ld[0])))
if mcd > 1:
  print(f'{str(int(nums[0] / mcd))}/{str(int(nums[1] / mcd))}')
else:
  print('This fraction is already at it\'s maximum reduction')

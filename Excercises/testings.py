nums = input().split()
#a = []
nums = list(int(x) for x in nums)
ld = []
for var in range(2):
  ld.append(list(f'{nums[var] / x:.1f}' for x in range(1,10)))
mcd = list(filter(lambda x: x in ld[1], ld[0]))
mcd = int(max(list(float(x) for x in mcd)))
print(f'{str(int(nums[0] / mcd))} {str(int(nums[1] / mcd))}')

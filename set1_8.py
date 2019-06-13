from math import gcd
from functools import reduce

mqr = input().split()
m = int(mqr[0])
q = int(mqr[1])

in_nums = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    g = reduce(gcd, in_nums[l-1:r])
    print(g)

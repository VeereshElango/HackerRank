import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    print("NO") if sum( [1 if x<=0 else 0 for x in a] ) >= k else print("YES")

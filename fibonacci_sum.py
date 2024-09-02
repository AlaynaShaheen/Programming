# Int FibonacciSum(int m, int n);
# Calculate and return the sum of Fibonacci numbers in the range from 'm' to 'n' (inclusive).
# Note: 0 < m <= n

import math
m=int(input())
n=int(input())
s=[0]*(n+1)
s[0]=0
s[1]=1
su=0
for i in range(2,n+1):
    s[i]=s[i-1]+s[i-2]
    if i>=m:
        su+=s[i]
print(su)

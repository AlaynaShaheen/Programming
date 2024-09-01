# The function accepts an integer array ‘arr’ of size ‘n’ as its argument. The function needs to
# return the index of an equilibrium point in the array, where the sum of elements on the left of the
# index is equal to the sum of elements on the right of the index. If no equilibrium point exists, the
# function should return -1.

n=int(input())
a=list(map(int,input().split()))
p=[0]
f=0
p.append(a[0])
for i in range(1,n):
    p.append(p[i-1]+a[i])
l=0;r=0
for i in range(n):
    l=p[i-1]
    r=p[n-1]-p[i]
    if l==r:
        f=i
        break
if f!=0:
    print(f)

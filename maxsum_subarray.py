# Given an array of integers, find the maximum subarray sum. A subarray is a contiguous
# subsequence of the array.

a=list(map(int,input().split()))
maxs=float('-inf')
curr=0
for i in range(len(a)):
    curr=curr+a[i]
    if maxs<curr:
        maxs=curr
    if maxs<0:
        maxs=0
print(maxs)
    

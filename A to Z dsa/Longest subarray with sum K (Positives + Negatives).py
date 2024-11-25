# Input: arr[] = [-1, 2, -3], k = -2
# Output: 3
# Explanation: The subarray [-1, 2, -3] has a sum of -2 and length 3.

class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        d=dict()
        s=0;m=-1
        for i in range(len(arr)):
            s+=arr[i]
            if s==k:
                m=max(m,i+1)
            if s-k in d:
                m=max(m,i-d[s-k])
            if s not in d:
                d[s]=i
        return m

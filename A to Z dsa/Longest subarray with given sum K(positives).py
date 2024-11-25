# Input: arr[] = [10, 5, 2, 7, 1, 9], k = 15
# Output: 4
# Explanation: The subarray [5, 2, 7, 1] has a sum of 15 and length 4.

class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        d=dict()
        s=arr[0];m=0
        i=0;j=0
        n=len(arr)
        while j<n:
            while i<=j and s>k:
                s-=arr[i]
                i+=1
            if s==k:
                m=max(m,j-i+1)
            j+=1
            if j<n:
                s+=arr[j]
        return m

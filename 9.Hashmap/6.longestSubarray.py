https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1


# User function Template for python3
from collections import defaultdict
class Solution:
    def longestSubarray(self, nums, k):  
        # code here
        # summ-k ->index -i+1
    #   -1  0  1  2  3  4  5
    #     [10, 5, 2, 7, 1, -10]
    #   0 10  15 17 24 25  15 
       
    #   store the first occ
       
       
        d = defaultdict(int)
        d[0] = -1
        summ =0
        maxi  =0
        n = len(nums)
        
        for ind in range(n):
            summ+=nums[ind]   #8
            
            if summ-k in d: #8-6 = 2
                maxi = max(maxi, ind - d[summ-k] )   #freq of 2 is 3 so cnt should be inc by 3
            
            if summ in d: #store the first occ
                continue
            else:
                d[summ] = ind 
        
        
        return maxi
 

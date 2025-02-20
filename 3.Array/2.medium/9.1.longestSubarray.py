https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k


from collections import defaultdict
class Solution:
    def longestSubarray(self, nums, k):  
        # code here
        # summ-k ->index -i+1
    #   -1  0  1  2  3  4  5
    #     [10, 5, 2, 7, 1, -10]
    #   0 10  15 17 24 25  15 
       
    #   store the first occ
    # [0,1,2,3, 4,5,6, 7 8]
    # [2,2,2,-4,1,3,2,-6,6] - arr
    # [2,4,6, 2,3,6,8,2, 8] - psum - use dict
    #  1            1
    # freq dynamically solve --> not precalculated
       
    #   note len is calucated from next index - ex - for 6-0 = 6 is ans and not 7 ( 1 to 6)
       
        d = defaultdict(int)
        d[0] = -1
        summ =0
        maxi  =0
        n = len(nums)
        
        for ind in range(n):
            summ+=nums[ind]   #8
            
            if summ-k in d: #8-6 = 2
                maxi = max(maxi, ind - d[summ-k] )   # 6-0 = 6   , d[2] = 0 as first occ
            
            if summ in d: #store the first occ if 8 in d ->dont store
                continue
            else:
                d[summ] = ind  #-> store the first oc of 8 ie ind = 6
        
        
        return maxi
 

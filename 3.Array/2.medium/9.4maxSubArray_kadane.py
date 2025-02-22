https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        maxi = nums[0]
        n = len(nums)
        for i in range(n):
            s = s + nums[i]
            maxi = max(maxi,s)
            if s<0:
                s=0
            
        return maxi

        '''
        # m1 - 3 for loops - bruteforce

        # m2 - 2 f loops - better - Time Limit Exceeded , O(N2)
        # maxi = float('-inf')
        # n = len(nums)
        # for i in range(0,n):
        #     sumj= 0
        #     for j in range(i,n):
        #         sumj= sumj + nums[j]
        #         maxi = max(maxi,sumj)
        # return maxi

        # m3 - optimal - KADANE ALGO 
        s=0
        maxi = nums[0] # - imp
        for i in range(len(nums)):
            s=s+nums[i]
            maxi = max(maxi,s)
            if s < 0:
                s=0
            # print(i, nums[i], s,maxi)
        return maxi
        '''

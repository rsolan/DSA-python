https://leetcode.com/problems/maximum-erasure-value/


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        se =set()
        summ =0
        maxi = 0
        for r in range(n):
            while nums[r] in se:
                se.remove(nums[l])
                summ-=nums[l]
                l+=1  #- place it end after remvoing and sub

            se.add(nums[r])
            summ+=nums[r]

            maxi = max(maxi,summ)

        return maxi

















        '''
        # max sum uniq el
        # VARIABLE SLIDING WINDOW - WHY -- subarray UNIQUE  
        n = len(nums)
        se = set()
        left = 0
        maxi = 0
        sumj = 0
        for right in range(n):
            while nums[right] in se:
                sumj = sumj - nums[left]
                se.remove(nums[left])
                left+=1
                

            se.add(nums[right])
            sumj = sumj+nums[right]

            maxi = max(maxi,sumj)

        return maxi
        '''






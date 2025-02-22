https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l =0
        r=0
        n = len(nums)
        mini = float('inf')
        s=0
        for r in range(n):
            s=s+nums[r]
            while s>=target:   #mini st insiside wihile lopp
                mini = min(mini,r-l+1)  # - there can still b asn of shorter len , after rmeoving 2,3,1,3
                s=s-nums[l]
                l+=1

        if mini ==float('inf'):
            return 0

        return mini

            








        '''
        # m1 - O(N)
        left =0
        n = len(nums)
        sumj =0
        mini = float('inf')
        for right in range(n):
            sumj = sumj + nums[right]

            # if sumj >= target: - no ans 

            # print(left,right,)

            while sumj >=  target:
                mini = min(mini, right-left+1)
                sumj = sumj - nums[left]
                left+=1

        if mini == float('inf'):
            return 0
        return mini


        '''
            

https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = 0 
        c=0
        for i in nums:
            if i == 0:
                # maxC = max(maxC,c)
                c=0
            else:
                c= c+1
            maxC = max(maxC,c) 
        return maxC



        #  lis = [] 
        # c=0
        # for i in nums:
        #     if i == 0:
        #         lis.append(c)
        #         c=0
        #     else:
        #         c= c+1
        # lis.append(c)
        # return max(lis)

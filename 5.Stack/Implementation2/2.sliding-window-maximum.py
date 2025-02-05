# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #         0 1  2  3 4
        # nums = [1,3,-1,-3,5,3,6,7], k = 3
        #                  i
        # q = [3 ]   #- dec order
        n = len(nums)

        q = []
        ans = []
        for i in range(n):
            # 1. index relveant - pop from front : POP WHEN FRONT IS LESS THAN EQ TO IND-K
            while q and q[0][0] <= i-k:  #for 3 0 is irrelevant
                q.pop(0)
            # 2 que in dec order , max at q top :POP FROM BACK IF BACK IS LESS THAN NUM[I]
            while q and q[-1][1] < nums[i]:
                q.pop()
            
            q.append([i,nums[i]])

            if i >= k-1:
                ans.append(q[0][1]) #q.front

        return ans

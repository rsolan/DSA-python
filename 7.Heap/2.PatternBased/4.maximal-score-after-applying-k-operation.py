# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # max heap 
        # repeat k times

        # pop the max - store it as score
        # insert back el/3
    
        heap =[]
        for i in nums:
            heapq.heappush(heap,-i)
        score =0
        while k:
            maxi = -heapq.heappop(heap)
            score = score+maxi
            heapq.heappush(heap,-ceil(maxi/3))
            # print(heap, score)
            k-=1


        return score

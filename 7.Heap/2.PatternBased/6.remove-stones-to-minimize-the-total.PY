https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/

import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # max heap

        heap =[]

        for i in piles:
            heapq.heappush(heap,-i)
        # print(heap)
        while k:
            maxi = -heapq.heappop(heap) 
            rem = maxi//2
            maxi = maxi-rem
            heapq.heappush(heap,-maxi)
            # print(heap)
            k-=1

        return -sum(heap)


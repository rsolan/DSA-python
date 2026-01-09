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

==with comments 
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # max heap - top pr max hoga , 
        # k operaion of inc score by maximum elements and then pushing back num/3

        score = 0
        heap =[]
        for i in nums:
            heapq.heappush(heap,-i) #form a max heap

        while k:  #imp condition 
            root = -heapq.heappop(heap)  # - imp as -(-10)
            score = score + root
            heapq.heappush(heap,-ceil(root/3)) # insert again neg element
            k-=1 #sub 

        return score



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

===
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        '''
        if we want min stones 
        we should remove max stones 
        since a operation can be done multiple time on a single pile - we want a pile to be in a heap after applying a operation

        max_heap = 9,5,4
        max -> 9 
        sub -> 9/2 = 4
        9-4 = 5
        put 5 back in heap 
        new heap = 5,5,4 ( max heapify)
        '''

        heap =[]
        # build a max heap 
        for i in piles:
            heapq.heappush(heap,-i)

        print(heap) #[-9, -4, -5] , [-7, -6, -4, -3]

        while k>0:
            maxi= -heapq.heappop(heap)
            new_el = maxi - (maxi//2) #// is floor division
            heapq.heappush(heap,-new_el)
            k-=1

        return -sum(heap)




        

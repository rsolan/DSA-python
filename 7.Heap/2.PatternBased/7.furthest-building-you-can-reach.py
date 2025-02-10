https://leetcode.com/problems/furthest-building-you-can-reach/

import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:


        # heights = [4,12,2,7,3,18,20,3,19], 
        #            0 8  0 5 0  15 2 0 16    - differnce
        # sequentially
        
        
        # bricks = 10, ladders = 2 - selection needs to be optimized
        n = len(heights)
        heap = [] #-store max diff for ladder - so use minheap
        flag = False
        # if not bricks and not ladders:
        #     return 0
        if n ==1:
            return 0
        # ind = 0

        # nlogn - size of heap can be n worst case  (log for insert/del)
        for ind in range(n-1):
            diff = heights[ind+1] - heights[ind]
            if diff>0:
                heapq.heappush(heap,diff)
                if len(heap)>ladders:
                    b = heapq.heappop(heap)
                    # print(b,bricks)
                    bricks=bricks-b
                    # print(ind, heap,bricks)
                    if bricks<0:
                        flag = True
                        break
                    
        if flag:
            return ind
        else:
            return ind+1   # n-1





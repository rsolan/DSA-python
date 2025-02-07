# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [3,2,1,5,6,4], k = 2

        heap = []
        # maintain min heap for largest el - as min el will be popped - and largest el will remain in heap
        # main min heap of k size
        # tc - nlogk ->faster than nlogn sorting tc
        # when n>>k - nlogk faster in comparison to nlogn

        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>k:
                heapq.heappop(heap)
        # print(heap)
        return heap[0]

# for kth smalelst  - use max heap of k size https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1
'''
import heapq

class Solution:

    def kthSmallest(self, arr,k):
        # for kth smalelst  - use max heap of k size
        heap =[]
        
        for i in arr:
            heapq.heappush(heap,-i)
            if len(heap)>k:
                -heapq.heappop(heap)
                
        return -heap[0]   #-- imp
        
  '''

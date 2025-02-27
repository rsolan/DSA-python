# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k =k
        self.nums = nums
        self.heap=[]
        for i in self.nums:
            heapq.heappush(self.heap,i)
            if len(self.heap)>self.k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # kth max score
        # maintain k size minheap
        
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

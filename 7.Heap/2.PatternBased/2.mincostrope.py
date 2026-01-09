# https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1

import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: list[int]) -> int:
    
        # code here
        heap =[]
        ans = 0
        sumj = 0
        
        for i in arr:
            heapq.heappush(heap,i)
            
        while len(heap)>1:  
            m1 = heapq.heappop(heap)
            m2 = heapq.heappop(heap)
            
            sumj = m1+m2
            
            # print(heap)
            if heap:   #otherwise infinite loop
                heapq.heappush(heap,sumj)
            
            ans = ans+sumj
        return ans
        
        
        # while heap: - ---------------1 vvimmppp will not work
        #     m1 = heapq.heappop(heap)
        #     if heap:  - ---------------3 vnot needed atall
        #         m2 = heapq.heappop(heap)
        #     sumj = m1+m2   4- wont work as m2 cant be addedd - so need extra check - cehcek 1
        #     # print(heap)
        #     if heap:
        #         heapq.heappush(heap,sumj)  - ---------------2 vvimmppp neededed 
           
        #     ans = ans+sumj
        # return ans

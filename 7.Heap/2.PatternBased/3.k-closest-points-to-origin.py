# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k not kth
        # k closest to origin - min dist to origin

        # we need max heap to store k closest points
        # max heap would be on the basis of eucldian dist
        # (dist,1,3)

        heap =[]

        for u,v in points:
            dist = ((u)**2 + (v)**2)**(1/2)  #dist of u,v from origin
            heapq.heappush(heap,(-dist,u,v))  #max heap so -dist
            # print(heap)
            if len(heap)>k:
                heapq.heappop(heap)

        # print(heap)
        out =[]
        while heap:
            dist,u,v = heapq.heappop(heap)
            out.append((u,v))

        return out


        




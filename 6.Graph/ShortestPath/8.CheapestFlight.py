'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

imp - not only cheapest but with constraint -- K STOPS ONLY 
so if in 2 stops - price is 400
but k =1 stop
and in 1 stop price is 700
i will return 700

find min price but with k stops

1. src and dst are not stops - middle point ar considered as stops
2. PQ - dist,node,stops
PQ DOES NOT WORK AS IT WILL PRIORITIZE MIN PRICE OVER K CONSTRAINt - it will incld min price with greater k instead of 
more price with less k
use Q - stops, node , cost - 
check <=k , till k is allowed staring from 0 as k can be dest

TC = E as onlye q  = flight size
'''
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # imp goal is not cheapest flight 
        # goal is with k constrant cheapest flight  -- USE QUEUE AND NOT PQ


        adj =[[] for _ in range(n)]
        for u,v,wt in flights:
            adj[u].append((v,wt))

        q = deque()
        q.append((0,src,0))  #stops, node, cost
        dist = [float('inf') for i in range(len(adj))]
        dist[src] = 0

        while q:
            stop,node,cost = q.popleft()
            if stop>k:  # skip teh curr iter if stops>k
                continue
            for v,wt in adj[node]:
                if cost + wt < dist[v] and stop<=k:  #-- imp <= as current dest also incl
                    dist[v] = cost+wt
                    q.append((stop+1,v,dist[v]))  #- inc the stop

        if dist[dst] == float('inf'):
            return -1
        return dist[dst]

'''
https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-weighted-undirected-graph
updat when dist is less
  store the parent [] to store node for each adj_node
                              then traverse in parent to form a list of list - to return who is coming from wehre
                              start from dest and backtrack
start from n to till parent become equal to node
push the src in lat 
reverse th path 

tc - dijkstra+path = elogv+n
'''
from typing import List
import heapq
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        adj=[[] for _ in range(n+1)]
        for u,v,wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))  #- imp as undir
            
        parent = [i for i in range(n+1)]  #-initialize with i or -1
        dist = [float('inf') for i in range(n+1)] #1 to n+1
         
        pq = []
        heapq.heappush(pq,(0,1))
        dist[1] = 0  #- start from 1st node -- 
        
        while pq:
            d,node = heapq.heappop(pq)
            
            for v,wt in adj[node]:
                if d+wt<dist[v]:
                    dist[v]  = d+wt
                    parent[v] = node
                    heapq.heappush(pq,(dist[v],v))
                    
        # Path reconstruction from node n to 1
        if dist[n] == float('inf'):  # No path exists to node n
            return [-1]  # Return -1 if no path exists
            
            
        ans =[]
        
        nd = n  #nd goes from n to 1
        while nd!=1:
            ans.append(nd)
            nd = parent[nd]
        ans.append(1)  #- src need loop breaks, but has to inc in ans path
        path = ans[::-1]
        return [dist[n]]+path

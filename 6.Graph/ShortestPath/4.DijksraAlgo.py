'''
shortest
using pq - min heap 
use set -- min at top ie ascending order 

using set - we can remove already existing paths(logn) high 10,5 and add 8,5
dist,node
'''https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1


import heapq
class Solution:
    
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        # Your code here
        # Note: The Graph doesn't contain any negative weight edge.
        # dj not work with negweigths and neg cycle AS INFINITE LOOP
        
        
        #  u->v,wt
        
        
        # m1 - use pq - minheap O(ELOGV - V2LOGV)
        
        pq = [(0,src)]
        heapq.heapify(pq)
        dist = [float('inf')  for _ in range(len(adj))]
        dist[src] = 0
        while pq:
            d,node = heapq.heappop(pq)
            
            for v,wt in adj[node]:
                if d+wt < dist[v]:
                    dist[v] = d+wt
                    heapq.heappush(pq,(dist[v],v))
                    
        return dist
        
        '''
        import heapq

        def dijkstra(V, adj, src):
            mh = []
            heapq.heappush(mh, (0, src))  # Min-Heap
            dist = [float('inf')] * V
            dist[src] = 0
        
            while mh:
                d, node = heapq.heappop(mh)  # Extract node with the smallest distance
        
                for v, wt in adj[node]:  # Relaxation
                    if d + wt < dist[v]:
                        dist[v] = d + wt
                        heapq.heappush(mh, (dist[v], v))  # Push updated distance
        
            return dist
        '''
        
        # m2 - use set -- NOT WORK IN PYTHON
        # s = set()
        # s.add((0,src))
        # dist = [float('inf')  for _ in range(len(adj))]
        # dist[src] = 0
        # while s:
        #     d,node = s.remove()
            
        #     for v,wt in adj[node]:
        #         if d+wt < dist[v]:
        #             dist[v] = d+wt
        #             s.add((dist[v],v))
                    
        # return dist
            
            

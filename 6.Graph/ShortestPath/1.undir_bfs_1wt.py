# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-undirected-graph-having-unit-distance

'''
use bfs - queeu is aleady sorted (we dont need any sorting algo - dist will inc by 1 edge ) O(V+2E)
src in que
dist is unit - so old dist +1
update only when smaller distance - and then push those neigh in que
unreachable nodes - inf - mark them as -1
'''
from collections import deque
class Solution:
    def shortestPath(self, adj, src):
        # code here
        # src to all vert
        
        # m1 - shortest path - so use dijkstra algo 
        
        # m2 - use bfs - q already sorted as distance wil linc by 1 at each level
        
        q = deque()
        q.append((src,0))  #node,dist
        dist =[float('inf') for i in range(len(adj))]
        dist[src] = 0
        while q:
            node,d = q.popleft()
            dist[node]  = d 
            for i in adj[node]:
                if d +1 < dist[i]:
                    dist[i] = d+1
                    q.append((i,dist[i]))
        for i in range(len(dist)):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist

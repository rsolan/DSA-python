'''
https://www.geeksforgeeks.org/problems/path-with-minimum-effort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=path-with-minimum-effort
shortest path , src, dest -use dijkstra
effort = max(abs diff of each node in a path from s to d)  - return min such effort to reach from src to dest

use PQ nd dist 2d array

pq - dist , row,col
push src 
while q
  tkae front 
  move in adj node s - l/r/u/d
  effort =  node(0) and adjnode(if greater than node ) - store the max of these diff ->psuh in PQ

O(ELOGV) - 4nm log (nm)
  
'''
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
    
        pq=[]
        heapq.heappush(pq,(0,0,0))  #dist,r,c  - dist i s0
        
        dist = [[float('inf')  for _ in range(m)] for _ in range(n)]
        dist[0][0] = 0
        delr =[-1,0,1,0]
        delc =[0,1,0,-1]
        while pq:
            d,row,col  = heapq.heappop(pq)
             # If we've reached the bottom-right corner, return the distance
            if row == n - 1 and col == m - 1:
                return d

            for i in range(4):
                nr = row+delr[i]
                nc = col+delc[i]
                if nr>=0 and nr<n and nc>=0 and nc<m:
                    newEffort = max(abs(heights[nr][nc] - heights[row][col]), d)  #- take max of old and diff
                    if newEffort <  dist[nr][nc]:  #update for new if max is smaller
                        dist[nr][nc] = newEffort
                        heapq.heappush(pq,(newEffort, nr, nc))

        return 0

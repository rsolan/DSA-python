'''https://leetcode.com/problems/shortest-path-in-binary-matrix/
https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-a-binary-maze

shortest path  -dijkrstra 
shortest path btw src and dest - can move l/r/u/d and move only when bit is 1
use 2d array for stroing dist - inf initialze (updated with dis - 0,1,2...)

put dist,dist - move 4 dir - store valid dist,node in PQ (update dist in 2d array)

NOTE - HERE Q can also work instead of PQ - bcoz dist wil inc by unit constant dist - so always in min fashion

edge case - when src = dest 
also return wrhenver u reach to dest 
else return -1

leetcode one is diff from gfg
'''

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # move only when 0 
        # move in 8 dir
        n = len(grid)
        m = len(grid[0])
        # If the starting or ending point is blocked, return -1 immediately.
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1

        if n ==1 and m==1:
            return 1  #- is src and dest is 0thindex --- imp it sdhould return 1 and not 0
        q = deque()
        q.append((1,0,0))  #dist,r,c
        
        dist = [[float('inf')  for _ in range(m)] for _ in range(n)]
        dist[0][0] = 0
        while q:
            d,row,col  = q.popleft()
             # If we've reached the bottom-right corner, return the distance
            if row == n - 1 and col == m - 1:
                return d

            for i in range(-1,2):
                for j in range(-1,2):
                    nr = row+i
                    nc = col+j
                    if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc] ==0 and d+1<dist[nr][nc]:
                        dist[nr][nc] = d+1
                        # if nr == n-1 and nc ==m-1: #standing on last index
                        #     return d+1
                        q.append((dist[nr][nc], nr, nc))

        return -1

# GFG https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find_the_number_of_islands

# sc - o(n2) for vis arr2d
# tc - o(n2) for for loop + 8xo(n2) bfs calls
from collections import deque

class Solution:
    def numIslands(self, grid):
        # code here
        # no of islands - no of connected component
        # any component - if nodes are connected (1s)- it will form 1 connected component
        
        # retunr connected components ie count of individual traversals
        
        # step2. bfs/dfs travesal - only  need is marking visited no dfs[] list needed
        def bfs_traversal(row,col):
            vis[row][col]=1
            q = deque()
            q.append((row,col))
            
            while q:
                r,c = q.pop()
                # traverse for all 8 neighbours
                for delrow in range(-1,2):
                    for delcol in range(-1,2):
                        nr = r+delrow
                        nc = c+delcol
                        if (nr>=0 and nr<n) and (nc>=0 and nc<m) and not vis[nr][nc] and (grid[nr][nc] ==1):
                            vis[nr][nc] =1
                            q.append((nr,nc))
                            
            
        
        # step1. if node = 0 nothing , innode = 1 do traversal if not already visited
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for j in range(m)] for i in range(n)]
        component_count= 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] ==1 and not vis[i][j]:
                    component_count+=1
                    bfs_traversal(i,j)
                    
        return component_count

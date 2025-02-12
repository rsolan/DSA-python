https://leetcode.com/problems/sort-matrix-by-diagonals/

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # Diagonals with exactly one element are already in order, so no changes are needed.
        # top - inc
        # bot inlc middle - dec
        '''
        x,y - which diag
        1,1 
        1,2 - top 

        2, 0 bottom 
        - 2,2 on right
        '''

        # 3
        # 0 2
        # -2

        # 0,1 - 1,2
        # -1      -1    -- diff of coord is same - that belongs to same diag

        # 0,0 1,1 2,2
        #  0   0   0

        # 1,0 - 2,1
        # 1      1

        # 4
        # 2,0
        # 2
        n = len(grid)
        m = len(grid[0])
        d={}
        for i in range(n):
            for j in range(m):
                if i-j in d:
                    d[i-j].append(grid[i][j])
                else:
                    d[i-j] = [grid[i][j]]

        # print(d)

        for i in d:
            if i>=0:
                d[i].sort(reverse = True)
            else:
                d[i].sort()
        # print(d)

        for i in range(n):   #--- traverse back and update as per key as
            for j in range(m):
                if i-j in d:
                    grid[i][j] = d[i-j].pop(0)
           
        # print(grid)
        
        return grid




        




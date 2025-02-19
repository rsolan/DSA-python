https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # m3 - optimal , conisder first row as colarray , first col as rowarray
        # tc - 2nm -> n2, sc - o(1)

        # a[0][0]-> wil be blocking so conisder once in rowarray , for collarray , colindex =0
        # traversing hre is key
        # 1. traverse without rowarray and colarray
        # 2, then traverse in colarray ->why
        # 3. then traverse in rowarray
        # rowarray=[0]*n --> a[..][0]  |
        # colarray = [0]*m --> a[0][..] --
        n = len(a)
        m = len(a[0])
        col_index =1
        #0. for all el , if 0 -> mark in fist row and col as 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    a[i][0] = 0  # rowarray[i]=1
                    if j!=0:
                        a[0][j] = 0  # colarray[j]=1
                    else:
                        col_index  =0 
        # 1. traverse from 1st row and 1st col , leave 0throw and 0thcol
        for i in range(1,n):
            for j in range(1,m):
                if a[i][j]!=0: #no worries for 0 el - as already 0 -.cant change them
                    if a[i][0]==0 or a[0][j] ==0:
                        a[i][j]=0
        
        # 2. first row depend on 0,0 el
        if a[0][0]==0:
            for j in range(m):
                a[0][j]=0
        # 3. first col depend on colindex
        if col_index ==0:
            for i in range(n):
                a[i][0]=0



        '''
        # m2 - nm x 1 +nm -> n2   , sc - o(n+m)
        n = len(a)
        m = len(a[0])

        rowarray=[0]*n  |
        colarray = [0]*m ---
        
        # nm
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    rowarray[i]=1 #- constant operation
                    colarray[j]=1
        # nm
        for i in range(n):
            for j in range(m):
                if rowarray[i] ==1 or colarray[j] == 1:
                    a[i][j] =0


        # m1 - nm x (n+m) +nm -> n3  +nm
        # if i == 0 then that row and col turns to 0 , not 0 but -1
        # but consider only original zeroes

        def makerow(r):
            for j in range(m):
                if a[r][j]!=0:
                    a[r][j] = -float('inf')

        def makecol(c):
            for j in range(n):
                if a[j][c]!=0:
                    a[j][c] = -float('inf')
        n = len(a)
        m = len(a[0])
        # nm
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    makerow(i) #-> n+m
                    makecol(j)
        # nm
        for i in range(n):
            for j in range(m):
                if a[i][j] == -float('inf'):
                    a[i][j] =0

        
'''



        

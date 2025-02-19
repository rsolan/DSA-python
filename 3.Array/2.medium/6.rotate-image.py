https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # m2 - inplace n2 ,no extr sapce
        # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

        # 1. transpose  -> only for top triangle - > swap a[i][j] with a[j][i] -n2
        n = len(a)
        m = len(a) #n,m are same here
        print(a)
        for i in range(0,n):
            for j in range(i+1,m): #---imp i+1 to n , 1 step next always   : i  to n also work
                a[i][j],a[j][i] = a[j][i],a[i][j]

        # 2. reverse rows -n
        for i in range(n):
            a[i].reverse()


        '''
        # i j   j n-1-i
        # 0       n-1-0
        # 0,0-> 0,2
        # 0,1-> 1,2
        # 0,2-> 2,2
        
        # 1       n-1-1
        # 1,0-> 0,1
        # 1,1-> 1,1
        # 1,2-> 2,1

        # 2       n-1-2
        # 2,0-> 0,0
        # 2,1-> 1,0
        # 2,2-> 2,0

        # m1 - 2x n2  , e xrra soace of on2
        n = len(a)
        ans=[[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[j][n-i-1] = a[i][j]

        # Copy ans back to a (in-place modification)
        for i in range(n):
            for j in range(n):
                a[i][j] = ans[i][j]  

        # or use a[:] = [row[:] for row in ans]
        '''

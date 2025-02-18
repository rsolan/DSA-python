https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

#User function Template for python3
class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        # code here
        #  4 ways fro all cells nm
        # tc - 4^(nm)

        # sc-o(nm) max rec depth - travel all cels
        
        n = len(mat)
        out =[]
        if mat[0][0]==0 or mat[n-1][n-1]==0:
            return out
            
        # since we want ans in lexiographically sorted - > we wil move in sorted order - > DLRU
        def rec(mat,vis,out,r,c,path):
            
            if r==n-1 and c == n-1:
                out.append(path[:])
                return
            
            stri  = 'DLRU'
            # drow =[-1,0,1,0]  #since check down first 
            # dcol = [0,1,0,-1]
            drow = [+1, 0, 0, -1]
            dcol = [0, -1, 1, 0]
            for ind in range(4):
                newr = r+drow[ind]
                newc = c+dcol[ind]
                if newr>=0 and newc>=0 and newr<n and newc<n and not vis[newr][newc] and mat[newr][newc]==1:
                    vis[r][c]=1   #r,c and not newr,newc
                    rec(mat,vis,out,newr,newc,path+stri[ind])   # newr,newc, path+stri[ind]
                    vis[r][c]=0

            
        vis = [[0 for _ in range(n)] for _ in range(n)]
        path =""
        rec(mat,vis,out,0,0,path)
        return out
        
        
        
        '''
        n = len(mat)
        out =[]
        if mat[0][0]==0 or mat[n-1][n-1]==0:
            return out
            
        # since we want ans in lexiographically sorted - > we wil move in sorted order - > DLRU
        def rec(mat,vis,out,r,c,path):
            
            if r==n-1 and c == n-1:
                out.append(path[:])
                return
            
            # downward
            if r+1<n and vis[r+1][c]==0 and mat[r+1][c]==1:
                vis[r][c]=1  #- make r,c visited as we visited it , not r+1,c
                rec(mat,vis,out,r+1,c,path+'D')  #- we can move to r+1,c
                vis[r][c]=0
                
            # left
            if c-1>=0 and vis[r][c-1]==0 and mat[r][c-1]==1:
                vis[r][c]=1  #- make r,c visited as we visited it , 
                rec(mat,vis,out,r,c-1,path+'L')  
                vis[r][c]=0
                
            # R
            if c+1<n and vis[r][c+1]==0 and mat[r][c+1]==1:
                vis[r][c]=1  #- make r,c visited as we visited it , 
                rec(mat,vis,out,r,c+1,path+'R')  
                vis[r][c]=0
                
            # U
            if r-1>=0 and vis[r-1][c]==0 and mat[r-1][c]==1:
                vis[r][c]=1  #- make r,c visited as we visited it , not r+1,c
                rec(mat,vis,out,r-1,c,path+'U')  #- we can move to r+1,c
                vis[r][c]=0
            
        vis = [[0 for _ in range(n)] for _ in range(n)]
        path =""
        rec(mat,vis,out,0,0,path)
        return out
        '''

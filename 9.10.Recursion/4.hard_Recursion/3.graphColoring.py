# User function Template for python3

https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1


class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        # MAX COLORS - M , can use les than m
        # try every color on every node - use recursion
        
        # tc - n^m for n nodes we try m colors
        # sc - n colro array +n depth of rec auxilary sapce
        graph =[[] for _ in range(v)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)  #-undir

        # print(graph) [[1, 2], [2], [3], [0]] - adj list
        
        def issafe(node,color,graph,n,c):
            for k in graph[node]: #adjacent nodes - neigh
                if color[k] == c:
                    return False
                    
            return True
                
        def rec(node,color,graph,n,m):
            if node == n:
                return True
                
            for i in range(m):
                if issafe(node,color,graph,n,i): # try all colors-i
                    color[node] = i # color the node wih i 
                    if rec(node+1,color,graph,n,m):
                        return True
                    color[node] = -1 #-- -1 not 0 , color it back 
                    
            return False #- not able to color this node with any color - false when not possible for all i
            
            
            
        n = len(graph) #- not edges
        color =[-1 for _ in range(n)]  #---vvimp -1 not 0
        if rec(0,color,graph,n,m):
            return True
        return False

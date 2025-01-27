from collections import deque

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: list[list[int]]) -> list[int]:
        # code here
        n = len(adj)
        vis = [0 for i in range(n)]
        vis[0]=1
        q = deque()
        q.append(0)  #standing on 0th node
        
        bfs =[]
        while q:
            node = q.popleft()
            bfs.append(node)
            
            for i in adj[node]:
                if not vis[i]:
                    vis[i] =1
                    q.append(i)
                    
        return bfs



class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        
        def dfs_fun(node):
            vis[node] = 1
            dfs.append(node)
            # traverse all neighbours - but hsould not be visited already
            for i in adj[node]:
                if not vis[i]:
                    dfs_fun(i)
            
        n = len(adj)
        dfs =[]
        vis =[0 for i in range(n)]
        dfs_fun(0)
        return dfs

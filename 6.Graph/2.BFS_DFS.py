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

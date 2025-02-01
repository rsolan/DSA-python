# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=direct-acyclic-graph

'''
1. adj list with weight
2. form a topo sort  using dfs stack  -- will give correct order to proces for  o(n+m)
3. take top of stack - for top node o(n+m)
d[node] +wt  < d[v] - so update
'''
class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # 1. FORM A TOPO SORT - WILL HAVE INC ORDER ALREADY - SO NO NEED OF DIJKSTRA
        # a. adj list Adjacency list of size V (number of vertices)
        adj = [[] for _ in range(V)]
    
        for u, v, wt in edges:  # Iterate through each edge
            adj[u].append((v, wt))  # Add directed edge u -> v with weight wt
            
        # print(adj)
        st =[]
        vis = [0 for i in range(V)]
        def dfs(node):
            vis[node] =1
            for i,wt in adj[node]:
                if not vis[i]:
                    dfs(i)
                    
            st.append(node)   #---imp node append
            
        for i in range(V):
            if not vis[i]:
                dfs(i)
        
        # now STACK HAS TOPO sort from top to end
        
        # 2. take a node out of stack one by one - relase the edges
        d = [10**9 for _ in range(V)]
        # src = st.pop()
        # d[st[-1]] = 0  #- imp take src node 0 - given d[0] = 0
        d[0] = 0
        
        while st:
            node = st.pop()
            
            for i,wt in adj[node]:
                if d[node] + wt < d[i]:
                    d[i] = d[node] +wt
        
        for i in range(len(d)):
            if d[i] == 10**9:
                d[i] = -1
                
        return d

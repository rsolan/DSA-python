# https://www.geeksforgeeks.org/problems/topological-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=topological-sort

#Function to return list containing vertices in Topological order. 
# STORE THE POPEL WHOSE DFS IS COMPLEETED - WHERE - IN STACK
    def topologicalSort(self,adj):
        # Code here
        # adjacency list for a Directed Acyclic Graph (DAG)
        
        # m1 - use dfs - to store ts we use stack
        # TC - O(V+E) directed graph, se - o(2n) st and vis
        n = len(adj)
        st =[]
        vis =[0 for i in range(n)]
        def dfs(node):
            vis[node] = 1
            for i in adj[node]:
                if not vis[i]:
                    dfs(i)
                    
            st.append(node)  #-- store node in stack after dfs call while returning
        
        
        for i in range(n):
            if not vis[i]:
                dfs(i)
        
        ans = []
        while st:
            node = st.pop()
            ans.append(node)
            
        return ans

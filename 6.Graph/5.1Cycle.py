from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		'''
		m2 - use dfs - store parent and if u reach back to same visited node but doesnt match the parent- the
		- there is cycle
		sc - o(n) - recursion stack space + o(n) vis
		tc - o(n+2e) for every node n -> u visited all adj (sum of adj = 2e)
		'''
		
		n = len(adj)
        vis = [0 for i in range(n)]
        
        
        def dfs_connectedComponents(node,parent):
            vis[node] =1
            
            for i in adj[node]: 
                if not vis[i]: 
                    #vis[i] = 1 #- doing at start of fun
                    if dfs_connectedComponents(i,node) == 1:   #-- vvvimp if u see a 1 , keep on returning1
                        return 1
                elif parent!= i:        
                    return 1
                        
            return 0
        
        # can be multiple components
        for i in range(n):
            if not vis[i]:
                if dfs_connectedComponents(i,-1) == 1:
                    return 1
                
        return 0

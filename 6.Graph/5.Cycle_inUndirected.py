from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		'''
        m1 - using bfs traversal - at each iteration goes to neighbours
        if at any time same no in queue twice - so there is cycle
        
        1 -> 0,2,4
        0->, 2->3 , 4 ->3
        so queue has 2 calss for 3 at same time - so there exist a cycle
        
        # tc - o(n+2e) for bfs fun + o(n) for n cals in for loop
        # sc - o(n)
	'''
		
        n = len(adj)
        vis = [0 for i in range(n)]
        q = deque()
        
        def bfs_connectedComponents(src):
            q.append((src,-1))  #- store node,parent
            vis[src] =1
            while q:
                node,parent = q.popleft() #4,1
                
                for i in adj[node]: # adj of 4 -> 1,3  ; 1 is vis and parent , 3 is visited and not parent
                    if not vis[i]: 
                        vis[i] = 1
                        q.append((i,node))
                    elif parent!= i:        #1!=1,3
                        # and vis  , 3 is visited by 2 and 3 is not parent of 4
                        #if someone is visited and its not a parent - means its been visited by other
                        return 1
                        
            return 0
        
        # can be multiple components
        for i in range(n):
            if not vis[i]:
                if bfs_connectedComponents(i) == 1:
                    return 1
                
        return 0
        

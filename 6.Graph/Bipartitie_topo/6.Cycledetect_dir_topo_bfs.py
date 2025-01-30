# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-a-directed-graph


#User function Template for python3
from typing import List
from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        
        # directed grapgh - on the same path---> NODE HAS TO BE VISITED AGAIN
        # undir - visite a adj node which is not a parent and already visiste d- issue - cycle detected
        
        # M2 - kAHNS ALGO - USING BFS 
        
        q = deque()
        n = len(adj)
        
        # 1.incoming nodes
        indegree =[0 for i in range(n)]
        for ilist in adj: 
            for j in ilist:
                indegree[j]+=1  #- adj[ind] has incoming edge to it
            
        # 2 store 0indegree el in queue
        for i in range(n):
            if indegree[i] ==0:
                q.append(i) 
                
        # 3.node -pop the q , reduce indegree of adj to node ; if indeg ==0 - pushin q
        cnt = 0
        while q:
            node = q.pop()
            cnt+=1
            # topo.append(node) #--NONEED OF TOPO - JUST NEED THE COUNT
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i] ==0:
                    q.append(i)
                    
        return cnt < n
        
        
        '''
        # M2 - kAHNS ALGO - USING BFS 
        
        q = deque()
        n = len(adj)
        topo =[]
        
        # 1.incoming nodes
        indegree =[0 for i in range(n)]
        for ilist in adj: 
            for j in ilist:
                indegree[j]+=1  #- adj[ind] has incoming edge to it
            
        # 2 store 0indegree el in queue
        for i in range(n):
            if indegree[i] ==0:
                q.append(i) 
                
        # 3.node -pop the q , reduce indegree of adj to node ; if indeg ==0 - pushin q
        while q:
            node = q.pop()
            topo.append(node) #--save node in my topological sort order
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i] ==0:
                    q.append(i)
                    
        return len(topo) < n  #cycle NOT exist if topo len ==n - FALSE, OTHERWISE TRUE
        '''
        
        
        '''
        # return false -if visited , path visietd 
        # m1 - DFS 
        n = len(adj)
        vis= [0 for i in range(n)]
        path_vis = [0 for i in range(n)]
        
        def dfs(node):
            vis[node] = 1
            path_vis[node]  = 1
            
            for i in adj[node]:
                if not vis[i]:  #not vis
                    if dfs(i) == True: #---imp check if any cycle detect - return T, no need to check othercall
                        return True
                elif path_vis[i]:  #visited and same path vis[i] and path_vis[i]
                    return True
                
            path_vis[node] = 0   #--imp step while going back for diff path , make currentpoath -0
            return False  #- cycle not detected
                    
        
        for i in range(n):
            if not vis[i]:
                if dfs(i) == True:  #- once a cycle detected - true - return - no need to check others
                    return True
                    
        return False
        '''
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
        print("~")
# } Driver Code Ends

# https://www.geeksforgeeks.org/problems/topological-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=topological-sort

from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        # Code here
        # adjacency list for a Directed Acyclic Graph (DAG)
        
        
        # M2 - kAHNS ALGO - USING BFS 
        # since bfs use q
        # tc - o(v+e) sc -- o(2n)
        q = deque()
        n = len(adj)
        topo =[]
        
        # 1.store indegree for all 
        # 5->0,2 means 0,2 has incoming edge towards it - so incby1
        indegree =[0 for i in range(n)]
        # for ind in range(n): 
        #     for j in range(len(adj[ind])):
        #         indegree[adj[ind][j]]+=1  #- adj[ind] has incoming edge to it
                
        for ilist in adj: 
            for j in ilist:
                indegree[j]+=1  #- adj[ind] has incoming edge to it
            
        # 2 store 0indegree el in queue
        for i in range(n):
            if indegree[i] ==0:
                q.append(i) #since i is node
                
        # 3.node -pop the q , reduce indegree of adj to node ; if indeg ==0 - pushin q
        while q:
            node = q.pop()
            topo.append(node) #--save node in my topological sort order
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i] ==0:
                    q.append(i)
                    
        return topo
            
            
        
        
        
        
        '''
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
        '''



#{ 
 # Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        e = int(input())
        adj = [[] for i in range(N)]

        for i in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)

        ob = Solution()

        res = ob.topologicalSort(adj)

        if check(adj, N, res):
            print(1)
        else:
            print(0)
        print("~")

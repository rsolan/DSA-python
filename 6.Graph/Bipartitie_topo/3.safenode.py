# https://www.geeksforgeeks.org/problems/eventual-safe-states/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=eventual-safe-states
# https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        # m1 - use cycle detect
        STORE ALL terminal nodes - no outgoing node , outdegree = 0

        safe node - ALL path from safe node should reach to terminal nodes

        everyone who is part of cycle , 
        anyone who is connected/leads (incomingwise) to a cycl ecan NEVER be a safe node
        rem node are safe node
        '''

        # m1 - cycle detected - DFS - vis, pathvis
        # sc - o3n, tc - o(v+e) 
        n = len(graph)
        vis= [0 for i in range(n)]
        path_vis = [0 for i in range(n)]
        safe = [0 for i in range(n)]
        
        def dfs(node):
            vis[node] = 1
            path_vis[node]  = 1
            
            for i in graph[node]:
                if not vis[i]:  #not vis
                    if dfs(i) == True: 
                        safe[node]  = 0
                        return True #- cycle detected thus not a safe node
                elif path_vis[i]:  #visited and same path
                    safe[node]  = 0
                    return True #- cycle detected thus not a safe node
                
            path_vis[node] = 0   
            safe[node]  = 1 #- node for which cycle not detected is my safe node
            return False  #- cycle not detected - so all path vis and no cycle thus safe node
                    
        # multicomponent
        for i in range(n):
            if not vis[i]:
                dfs(i) #- make call for all i, no true/false

        # take ans as safe node ==1
        ans =[]
        for i in range(len(safe)):
            if safe[i]==1:
                ans.append(i) #those index nodes whose val is 1

        return ans

            

        
                    
        

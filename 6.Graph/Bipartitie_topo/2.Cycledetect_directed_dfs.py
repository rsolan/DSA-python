# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-a-directed-graph

#Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        
        # directed grapgh - on the same path---> NODE HAS TO BE VISITED AGAIN
        # undir - visite a adj node which is not a parent and already visiste d- issue - cycle detected
        
        
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

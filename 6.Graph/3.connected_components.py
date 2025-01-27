class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #  no of connected compononets - traverse(3)- 3 starting nodes - > 3 travesal call - just count them
        # how to get 3 - count it 

        # 1. form adj_list out of edges -
        adj_list =[[] for i in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # 3. traversal - bfs or dfs - just need to update the visisted array
        def dfs_fun(st_node):
            vis[st_node] = 1
            # dfs.append(st_node)          
            for neigh in adj_list[st_node]:
                if not vis[neigh]:
                    dfs_fun(neigh)

        # 2. count = no of times dfs travesal gone - no of connected components 
        connected_count = 0
        vis = [0 for i in range(n)]
        for i in range(n):
            if not vis[i]:
                connected_count +=1
                dfs_fun(i)

        return connected_count
      

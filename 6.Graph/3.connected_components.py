
# leetcode 323, 547

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #  no of connected compononets - traverse(3)- 3 starting nodes - > 3 travesal call - just count them
        # how to get 3 - count it 
# similar quest - https://leetcode.com/problems/number-of-provinces/
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
      


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # return no of connected components
# similar ques - https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
        # starting node = 1, also if its conencted to itself - val i s1
        #  no of connected compononets - traverse(3)- 3 starting nodes - > 3 travesal call - just count them
        # how to get 3 - count it 


        # 1.we are given adj matrix - create adj_list out of it
        n = len(isConnected)
        m = len(isConnected[0])
        adj_list =[[] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i!=j and isConnected[i][j]==1:
                    adj_list[i].append(j)

        print(adj_list) #- take care can be 0 or 1 indexed - choose/stick to one of them

#   0    1    2      
# [[1], [0], []]
        # 3. traversal - bfs or dfs - just need to update the visisted array
        def dfs_fun(st_node):
            vis[st_node] = 1
            # dfs.append(st_node)          
            for neigh in adj_list[st_node]:
                if not vis[neigh]:
                    dfs_fun(neigh)

        # 2. count = no of times dfs travesal gone - no of connected components 
        province_count = 0
        vis = [0 for i in range(n)]
        for i in range(n):
            if not vis[i]:
                province_count +=1
                dfs_fun(i)

        return province_count






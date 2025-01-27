class Solution:
    def count(self, n):
        # Calculate the total number of possible edges
        total_edges = (n * (n - 1)) // 2
        # Calculate the number of possible graphs
        return 2 ** total_edges


# adjacency list representation
class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here
        adj_list = [[] for _ in range(V)]
        
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        return adj_list


# 1.we are given adj matrix - create adj_list out of it - https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
        n = len(isConnected)
        m = len(isConnected[0])
        adj_list =[[] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i!=j and isConnected[i][j]==1:
                    adj_list[i].append(j)

        print(adj_list) #- take care can be 0 or 1 indexed - choose/stick to one of them

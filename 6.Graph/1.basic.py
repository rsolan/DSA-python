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

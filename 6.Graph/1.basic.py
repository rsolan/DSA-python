class Solution:
    def count(self, n):
        # Calculate the total number of possible edges
        total_edges = (n * (n - 1)) // 2
        # Calculate the number of possible graphs
        return 2 ** total_edges

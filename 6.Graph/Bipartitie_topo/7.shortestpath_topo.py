# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=direct-acyclic-graph

'''
1. adj list with weight
2. form a topo sort  using dfs stack  -- will give correct order to proces for  o(n+m)
3. take top of stack - for top node o(n+m)
d[node] +wt  < d[v] - so update
'''

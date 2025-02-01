# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-undirected-graph-having-unit-distance

'''
use bfs - queeu is aleady sorted (we dont need any sorting algo - dist will inc by 1 edge ) O(V+2E)
src in que
dist is unit - so old dist +1
update only when smaller distance - and then push those neigh in que
unreachable nodes - inf - mark them as -1
'''

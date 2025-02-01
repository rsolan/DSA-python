'''
https://www.geeksforgeeks.org/problems/path-with-minimum-effort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=path-with-minimum-effort
shortest path , src, dest -use dijkstra
effort = max(abs diff of each node in a path from s to d)  - return min such effort to reach from src to dest

use PQ nd dist 2d array

pq - dist , row,col
push src 
while q
  tkae front 
  move in adj node s - l/r/u/d
  effort =  node(0) and adjnode(if greater than node ) - store the max of these diff ->psuh in PQ

O(ELOGV) - 4nm log (nm)
  

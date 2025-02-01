'''https://leetcode.com/problems/shortest-path-in-binary-matrix/
https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-a-binary-maze

shortest path  -dijkrstra 
shortest path btw src and dest - can move l/r/u/d and move only when bit is 1
use 2d array for stroing dist - inf initialze (updated with dis - 0,1,2...)

put dist,dist - move 4 dir - store valid dist,node in PQ (update dist in 2d array)

NOTE - HERE Q can also work instead of PQ - bcoz dist wil inc by unit constant dist - so always in min fashion

edge case - when src = dest 
also return wrhenver u reach to dest 
else return -1
'''

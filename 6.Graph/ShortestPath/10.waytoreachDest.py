'''
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/

return no of path with shortest dist , path can be more than1

ways to raech node doesnt inc by 1 always , bcoz paren noe would have ben reach in more than 1 way
so ways[n] = ways[p1] + ways[p2]+..  
(not 1+1+..)

if at ant node 
large dist than current - ignore
equal dist - in no of ways by parent ways (not by 1) - NO PUSH IN PQ
if less dist - reset the current no of ways -> as old ways were for large dist , and store the new ways of parent - push in Q            - if old ways were 0 - means first time coming so push in Q


O(ELOGV) - DIJKSTRA
'''

from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # visite a adj node which is not a parent and already visiste d- issue - cycle detected
        # https://www.geeksforgeeks.org/problems/bipartite-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bipartite-graph

        # m2 - dfs
        n  = len(graph)
        vcolor = [-1 for  i in range(n)]

        def dfs(node,col):
            vcolor[node] = col
            for neigh in graph[node]:
                if vcolor[neigh] == -1: #notvis
                    if dfs(neigh,not col) == False:  #------vvvvimp dfs calss are returned if false - need tocheck
                        return False

                elif vcolor[neigh] == vcolor[node]: #neigh visited and has same color as of current node
                    return False

            return True

        for i in range(n): #for multicomponents
            if vcolor[i] == -1:
                if dfs(i,0) == False:   #--sending src with color = 0
                    return False

        return True

        '''
        # m1 - using bfs
        n  = len(graph)
        vcolor = [-1 for  i in range(n)]

        def bfs(src):
            q = deque()
            q.append(src)
            vcolor[src] = 0

            while q:
                node = q.popleft()
               
                for neigh in graph[node]:
                    if vcolor[neigh] == -1: #notvis
                        vcolor[neigh]  = not vcolor[node]
                        q.append(neigh)
                    elif vcolor[neigh] == vcolor[node]: #neigh visited and has same color as of current node
                        return False #- cycle detected
            return True

        for i in range(n): #for multicomponents
            if vcolor[i] == -1:
                if bfs(i) == False:  #- cycle detected and thus not bipartite
                    return False

        return True
        '''

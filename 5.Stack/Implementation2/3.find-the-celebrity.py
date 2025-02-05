# https://leetcode.com/problems/find-the-celebrity/description/
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # M2 - 2POINTER
        # candidate = None
        s = 0
        e = n-1
        while s<e:
            if knows(s,e):
                # candidate = e
                s+=1
            else:
                # candidate = s
                e-=1

        if s>e:
            return -1 #when no celeb
        candidate = s
        # if a single el is left - check that if ans or not
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate,i) or not knows(i,candidate):   #--or
                return -1

        return candidate


'''
        # m1 - bruteforce - TLE
        knowme=[0]*n
        iknow=[0]*n
        # col    0 1 2
        # row 0 [1,1,0]

        for i in range(n):
            for j in range(n):
                if i!=j and knows(i,j) ==1: #graph[i][j] == 1:
                    iknow[i]+=1
                    knowme[j]+=1

        # print(iknow,knowme)
        for i in range(n):
            if knowme[i] ==n-1 and iknow[i] ==0:
                return i
        return -1
'''
        

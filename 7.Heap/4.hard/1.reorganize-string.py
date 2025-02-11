https://leetcode.com/problems/reorganize-string/description/

import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:

        # aaab

        # a 3
        # b 1

        # aaaa bbbb cc d e

        # ababababcdce
        # prev = None  b,0
        # heap = [   ,   c,-2]
        # a,0
        # aba

        # high freq - but we dont 


        # max heap = [a]
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        heap =[]
        for i in d: 
            heapq.heappush(heap,(-d[i], i))  #-freq,val -> max heap
        prev = None
        ans = ""
        while heap:
            f,v=heapq.heappop(heap)
            ans+=v
            f+=1    #-- -3+1 = -2 so we are reducing only but use + as neg values
            if prev:
                heapq.heappush(heap,prev)
            if f!=0:
                prev = (f,v)
            else:
                prev = None  #- -in case freq is 0 - no need ot put it back

        if len(ans) == len(s):
            return ans
        else:
            return ""
        # print(ans)













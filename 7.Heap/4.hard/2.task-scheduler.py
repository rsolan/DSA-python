https://leetcode.com/problems/task-scheduler/

import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # m2 -use dict 
        d={}
        for i in tasks:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        heap=[] #maxheap
        for i in d:
            heapq.heappush(heap,(-d[i],i))  #-freq,val
        print(heap)

        d1={}
        t = 0
        while heap or d1:
            if t in d1:
                heapq.heappush(heap,(d1[t][0],d1[t][1]))  #-- d1[ind] = freq,val
                del d1[t]

            if heap:
                f,v = heapq.heappop(heap)
                f+=1
                if f!=0:
                    d1[t+n+1] = (f,v)
                    
            t+=1
    

        return t


'''
        # m1 - # o(nlogn)
        # 1 consecutive - we used prev

        # A:3 , B:3


        # PREV = A:3,nextt  ; B:3,t  - we want queue or dict - keeping index as prioirty 
        d={}
        for i in tasks:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        print(d)

        heap=[]
        for i in d:
            heapq.heappush(heap,(-d[i],i))  #-freq,val
        print(heap)

        queue=[]
        out =""
        t = 0
        while heap or queue:
            
            if queue and queue[0][2] == t:
                popf,popv,popt = queue.pop(0)
                heapq.heappush(heap,(popf,popv))

            if heap:
                f,v = heapq.heappop(heap)
                # out+=v - noneed
                f+=1
                if f!=0:
                    queue.append((f,v,t+n+1))
                # else:
            t+=1
            

        # print(t)

        return t
                
'''


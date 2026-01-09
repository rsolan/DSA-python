# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most freq 
        # return k size min heap - on ethe basis of freq
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        # l = list(d.items()) - no need 
        # print(l)

        heap=[]
        for val,freq in d.items():  #-- imp use d.items()
            heapq.heappush(heap,(freq,val)) #-------push freq first param - as min freq will be pop
            if len(heap)>k:
                heapq.heappop(heap)

        # print(heap)
        out =[]
        for freq,val in heap:
            out.append(val)

        return out


===
with comemnts
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d = (i,freq)----imp use dict

        d={}
        n= len(nums)
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1

        # print(d) 
        # {1: 3, 2: 2, 3: 1},   {1: 1} ,    {1: 4, 2: 4, 3: 2}

        heap =[]
        #make min heap , pop min freq el, keep k max freq el in heap


        # for i in d:
            # print(i,d[i]) 1,3

        for val,freq in d.items():
            heapq.heappush(heap,(freq,val)) #not v,f
            if len(heap)>k:
                heapq.heappop(heap)
        out=[]
        while heap:
            freq,val = heapq.heappop(heap)
            # we can just traverse also instead of pop-> for frq,val in heap , out.append(v)
            out.append(val)

        return out







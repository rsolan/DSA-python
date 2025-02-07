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

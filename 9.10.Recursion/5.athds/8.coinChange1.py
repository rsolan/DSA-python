https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, c: List[int], t: int) -> int:
        # coins = [1,2,5]

        out =[]
        ds=[]
        n = len(c)
        d = [[-1 for _ in range(t+1)] for _ in range(n+1)]
        
        def rec(i,s):
            if i == n and s==t:
                return 0 
                
            if i==n or s>t:
                return float('inf')

            if d[i][s] != -1:
                return d[i][s]

            take = rec(i,s+c[i]) + 1
            nottake = rec(i+1,s) + 0

            d[i][s] = min(take,nottake) 

            return d[i][s]

        ans = rec(0,0)
        if ans ==float('inf'):
            return -1
        return ans



        '''

        out =[]
        ds=[]
        n = len(c)
        
        def rec(i,s):
            if i == n and s==t:
                return 0 
                
            if i==n or s>t:
                return float('inf')
            
            take = rec(i,s+c[i]) + 1
            nottake = rec(i+1,s) + 0

            return min(take,nottake)  #comp in reverse

        ans = rec(0,0)
        if ans ==float('inf'):
            return -1
        return ans



        out =[]
        ds=[]
        n = len(c)
        global mini
        mini = float('inf')
        def rec(i,ds,s):
            global mini
            if i == n and s==t:
                mini = min(mini,len(ds))
                return
            if i==n or s>t:
                return 

            ls1 = ds[:]
            ls2 = ds[:]

            ls1.append(c[i])
            take = rec(i,ls1,s+c[i]) + 1
            nottake = rec(i+1,ls2,s) + 0

        rec(0,ds,0)
        if mini ==float('inf'):
            return -1
        return mini


        out =[]
        ds=[]
        n = len(c)

        def rec(i,ds,s):
            if i == n and s==t:
                out.append(ds[:])
                return
            if i==n or s>t:
                return 

            ls1 = ds[:]
            ls2 = ds[:]

            ls1.append(c[i])
            rec(i,ls1,s+c[i])
            rec(i+1,ls2,s)

        rec(0,ds,0)
        # print(out)
        mini = float('inf')
        for i in out:
            mini = min(mini,len(i))
        if mini ==float('inf'):
            return -1
        return mini
        '''
        


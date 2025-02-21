https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, t: int, c: List[int]) -> int:
        # 2+2+1
        # 122
        # duplicate combinations


        out = []
        ds=[]
        n =len(c)
        # s = amount
        d = [ [-1 for i in range(t+1)] for j in range(n+1)]  # always take range +1
        # n rows , s cols
        # d[n][t] 

        # dict is slower than tabular approach
        
        def rec(i,s):
            if i==n and s==t:
                return 1

            if i==n or s>t:
                return 0
            if d[i][s] != -1:    # o(1) , since index is known faster to check in 2d arr , instead of dict
                return d[i][s]

            # d[i][s] -> take n variables which are changing -> that many comb

            take = rec(i,s+c[i])

            nottake = rec(i+1,s)

            d[i][s] = take+nottake

            return d[i][s]
        
        return rec(0,0)



        '''
        # dp
        out = []
        ds=[]
        n =len(c)
        d={}
        # dict is slower than tabular approach
        
        def rec(i,s):
            if i==n and s==t:
                return 1

            if i==n or s>t:
                return 0
            if (i,s) in d:    #key:val   , (i,s): cnt
                return d[(i,s)]


            take = rec(i,s+c[i])

            nottake = rec(i+1,s)

            d[(i,s)] = take+nottake

            return d[(i,s)]
        
        return rec(0,0)
        '''

        # rec
        







        '''

        out = []
        ds=[]
        n =len(c)
        
        def rec(i,s):
            if i==n and s==t:
                return 1

            if i==n or s>t:
                return 0

            take = rec(i,s+c[i])

            nottake = rec(i+1,s)

            return take+nottake
            # return rec(i,s+c[i]) + rec(i+1,s)
        
        return rec(0,0)




        out = []
        ds=[]
        n =len(c)
        global cnt
        cnt = 0
        def rec(i,s):
            global cnt
            if i==n and s==t:
                cnt+=1
                return

            if i==n or s>t:
                return

            rec(i,s+c[i])

            rec(i+1,s)
            
        rec(0,0)
        return cnt




        out = []
        ds=[]
        n =len(c)

        def rec(i,ds,s):
            if i==n and s==t:
                out.append(ds[:])

            if i==n or s>t:
                return

            ls1 = ds[:]
            ls2 = ds[:]

            ls1.append(c[i])
            rec(i,ls1,s+c[i])

            rec(i+1,ls2,s)
            
        rec(0,ds,0)
        return len(out)
        '''






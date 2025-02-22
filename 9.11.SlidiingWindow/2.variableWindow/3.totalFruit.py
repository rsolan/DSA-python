https://leetcode.com/problems/fruit-into-baskets/


class Solution:
    def totalFruit(self, f: List[int]) -> int:

        n = len(f)
        d={}
        l=0
        r=0

        maxi = 0
        for r in range(n):
            if f[r] in d:
                d[f[r]]+=1
            else:
                d[f[r]]=1

            while len(d)>2:  #-- should be atter why??  - bcoz dict ??
                d[f[l]]-=1
                if d[f[l]] ==0:
                    del d[f[l]]
                l+=1


            maxi = max(maxi,sum(d.values()))

        return maxi

	


        '''
        # VAR SLIDING WINDOW == USE DICT AND NOT SET 
        left = 0
        n = len(fruits)
        d={}
        cnt =0
        maxi =0
        for right in range(n):
            if fruits[right] in d:
                d[fruits[right]]+=1
                cnt+=1
            else:
                d[fruits[right]]= 1
                cnt+=1

            while len(d) >2:
                d[fruits[left]]-=1 #start removing 1by1 from left
                cnt-=1
                if d[fruits[left]] ==0 :  #del fruit type who becomes zero first
                    del d[fruits[left]]

                left+=1
            
            # maxi = max(maxi, right-left+1)
            # maxi = max(maxi,sum(d.values)) #since only 2 values
            maxi = max(maxi,cnt)

        return maxi
        '''

        

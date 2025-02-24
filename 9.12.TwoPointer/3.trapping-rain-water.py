https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        # min height
        # ````````min(leftmax, rightmax) - current
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        #    i   j

        # find leftmax, rightmax 
        # min(leftmax,rightmax) - current height -- all should be greater than 0
        # neg scenario - as no water stored 
        '''
        # m1 - bruteforce - o(n2) -- TLE
        n = len(height)
        ans = 0
        # sumj = 0
        for ind in range(n):
            maxl = 0
            maxr = 0

            for i in range(ind+1,n):
                maxr= max(maxr,height[i])

            for i in range(ind):
                maxl = max(maxl,height[i])

            ans += max(min(maxl,maxr)-height[i],0)   #- handling neg case
            # ans = min(maxl,maxr) - height[ind]
            # if ans>=0:
            #     sumj = sumj + ans

        return sumj
        '''

        
        # m2  tc - o(3n) sc - o(2n)
        # [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        # [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
        # [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
        # preprocess prefix max and suffix max 
        n  =len(height)
        p = 0
        prefix_max =[]
        for i in range(n):
            prefix_max.append(p) # keep p and then update it - not incl current index
            p = max(p,height[i])
        
        p = 0
        suffix_max =[]
        for i in range(n-1,-1,-1):
            suffix_max.append(p)
            p = max(p,height[i])
        suffix_max.reverse() #--impppp
        print(height)
        print(prefix_max)
        print(suffix_max)
        ans = 0
        for i in range(n):
            ans += max(min(prefix_max[i],suffix_max[i])-height[i],0)

        return ans
        

        # m3 - O(N) - 2 pointer - tough
        # since we want min of lmax and rmax
        # we cehck in if-else if lmax<=rmax - and then that one only
        i = 0
        n = len(height)
        j = n-1
        leftmax = 0
        rightmax = 0
        ans = 0
        while i<=j:
            if leftmax<=rightmax:
                ans += max(leftmax - height[i],0)   #- taking lmax only
                leftmax = max(leftmax,height[i]) 
                i+=1 #move i 

            else:
                ans += max(rightmax - height[j],0) 
                rightmax = max(rightmax,height[j])
                j-=1 #move j

        return ans











        



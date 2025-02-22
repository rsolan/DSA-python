https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # m1 - bruteforce - TLE
        # n = len(nums)
        # maxi = - float('inf')
        # for i in range(n):
        #     p  =1
        #     for j in range(i,n):
        #         p = p*nums[j]
        #         maxi = max(maxi,p)

        # return maxi


        # m2 - 
        # 1. all pos - return prod of all
        # 2. even neg - retunr prod of all

        # 3. odd neg -> remove 1 neg , and return prod of all

        # which neg to remove min neg , it will add few to prod , when taken as even neg

        # NO need to from subarrays
        # remove 1 neg , left and right will be either 1 or 2; if its 3 its bad split

        # so ans is prefox or suffix product for neg numbers - no ned to calcualte line iwse
        # return thr maxi of pref and suff
        # [3,2,-1,4,-6,3,-2,6]
        # n = len(nums)
        # maxi = -float('inf')
        # p = 1
        # for i in nums:
        #     p=p*i
        #     maxi = max(maxi,p)
        #     if p == 0:
        #         p =1  
            

        # s= 1
        # for i in range(n-1,-1,-1):
        #     s=s* nums[i]
        #     maxi = max(maxi,s)
        #     if s == 0:         # edgec ase - 0 can make prod 0 , so make p = 1 ie start fresh prod

        #         s =1
        # return maxi   


        # m3 - bit optimal in 1 pas    
        n = len(nums)
        maxi = -float('inf')
        p = 1
        s = 1
        for i in range(n):
            if p ==0: p =1
            if s==0: s=1
            p=p*nums[i]
            s=s*nums[n-i-1] #use last inedx and 0th index side by side 
            maxi = max(maxi,max(p,s))
  
        return maxi  

        


        

















        

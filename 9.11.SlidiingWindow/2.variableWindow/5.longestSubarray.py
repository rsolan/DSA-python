https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        #count of 0s can be 1 

        cnt0 =0
        l =0
        r=0
        n = len(nums)
        maxi = 0

        for r in range(n):
            if nums[r]==0:
                cnt0+=1
            
            while cnt0>1:	
                if nums[l]==0:
                    cnt0-=1
                l+=1		 #--- to do this after reducing

            maxi = max(maxi,r-l+1)

        return maxi-1  #imp

        '''
        
        # no need of cnt
        n = len(nums)
        left = 0
        cnt = 0
        cnt0 = 0
        maxi = 0
        for right in range(n):

            if nums[right] ==0:
                cnt0+=1
            else:
                cnt+=1

            while cnt0>1:
                if nums[left] == 0:
                    cnt0-=1
                else:
                    cnt-=1
                left+=1

            maxi = max(maxi,right-left+1)  #dont use cnt as cant differentiate btw all 1s and with 0s

        return maxi-1 #-- imp not maxi as delete 1 el
#                                         r
#  Input: nums = [ 1, 1, 0,1,1,1,0,1,1,0,1]
#                                  l

'''
            

        

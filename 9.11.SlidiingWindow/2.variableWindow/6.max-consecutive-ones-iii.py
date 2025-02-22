https://leetcode.com/problems/max-consecutive-ones-iii/description/


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        cnt0 =0
        l =0
        r=0
        n = len(nums)
        maxi = 0

        for r in range(n):
            if nums[r]==0:
                cnt0+=1
            
            while cnt0>k:	
                if nums[l]==0:
                    cnt0-=1
                l+=1		 #--- to do this after reducing

            maxi = max(maxi,r-l+1)

        return maxi  #imp


        '''
        n = len(nums)
        left = 0
        cnt = 0
        cnt0 = 0
        maxi = 0
        for right in range(n):

            if nums[right] ==0:
                cnt0+=1
            # else:
            #     cnt+=1

            while cnt0>k:
                if nums[left] == 0:
                    cnt0-=1
                # else:
                #     cnt-=1
                left+=1

            maxi = max(maxi,right-left+1)  #dont use cnt as cant differentiate btw all 1s and with 0s
# cant use cnt - what to add cnt0+cnt1?
        return maxi

        '''

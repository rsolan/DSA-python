https://leetcode.com/problems/subarray-product-less-than-k/


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        #start removing if prod greater than k  ;not including =
#contigous

        l =0
        r=0
        n = len(nums)
        ans = 0

        if k ==0:  #--->edgecase p can never be less than k , all pos and k = 0 
            return 0
        p =1
        for r in range(n):
            p=p*nums[r]
            
            while p>=k and l<=r:  #incl = sign and why l<=r
                p=p//nums[l]
                l+=1

            ans = ans + (r-l+1)

        return ans

        # [10,5,2,6]
        # [10] - > r-l+1 = 0-0+1 = 1  [10]
        # adding a new 5 includes 2 more response = [10,5] and [5]
        # [10,5] -> r-l+1 = 1-0+1 2 ans 
        # ans = 3 tilr [10,5]

	

        '''
        # store the len as ans -- as for intermdeiate arrays count will be equal to length till that point  r-l+1
        n = len(nums)
        left =0
        p =1
        ans = 0
        cnt = 0
        if k ==0:  # - edge case - all VALUES GREATER THAN K
            return 0
        for right in range(n):
            p = p*nums[right]

            while p>=k and left<=right:  # - LEFT WILL MOVE MORE THAN RIGHT -- NEVER COME OUT OF LOOP-why?
                p = p//nums[left]
                left+=1

            ans = ans + (right-left+1)  #= why add  r-l+1 --- vvvimp

        return ans
        '''
           
                

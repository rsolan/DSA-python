https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find first 0th inex, navigate swap nonzero with zero
        j = -1
        n = len(nums)
        for ind,val in enumerate(nums):
            if val ==0:
                j = ind
                break
        if j ==-1:  #---e dge case
            return nums
        
        for i in range(j+1,n):
            if nums[i]!=nums[j]:
                nums[i],nums[j]= nums[j],nums[i]
                j+=1
        

        '''
        # # m1 - use extra space o(n), tc - o(2n) 
        # o=[]
        # count = 0
        # for i in nums:
        #     if i!=0:
        #         o.append(i)
        #     else:
        #         count+=1

        # while count!=0:
        #     o.append(0)
        #     count-=1

        # for i in range(len(o)):
        #     nums[i]=o[i]




        # m1' - no need to count 0  - O(2N) , sc - O(N)
        # o=[]
        # n = len(nums)
        # for i in nums:
        #     if i!=0:
        #         o.append(i)
        # for i in range(len(o)):
        #     nums[i]=o[i]

        # for i in range(len(o),n):
        #     nums[i]=0




        # m2 - OPTIMAL - USE 2 POINTER APPROACH tc - o(n) , sc - o(1)
        
        j=-1
        n= len(nums)
        # find j - as first zero index
        for ind in range(n):
            if nums[ind] == 0:
                j= ind
                break
        if j ==-1:
            return nums # no zeroes in nums - edge case
        
        for i in range(j+1,n):
            if nums[i]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
                
        # j will always stand at 0
        # 12, 23, 12, 0,1,0,3,12
        #             j 
        #               i

        # 12, 23, 12, 1,3,12,0,0
        #                 j      i
        '''

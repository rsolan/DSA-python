https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

class Solution:
    def check(self, nums: List[int]) -> bool:

        # array is sorted rotated - if it has only 1  dip
        n = len(nums)
        dip =0
        if nums[0] < nums[-1]: #0th indx
            dip+=1
        for i in range(1,n): #1st index to n
            if nums[i] < nums[i-1]:  
                dip+=1
            
            if dip>1:
                return False

        return True


        '''
        [3,4,5,1,2]
         i j
        drop when i+1<i , false if mpre than 1 drop
        

        count = 0
        n = len(nums)
        # edge case - for 1st and last el
        if nums[0] < nums[n-1]:
            count+=1
        for i in range(n-1):
            if nums[i+1] < nums[i]:
                count+=1
            if count>1:
                return False

        return True
        '''
            

        


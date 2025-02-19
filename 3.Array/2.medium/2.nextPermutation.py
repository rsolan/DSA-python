https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        test case
                   i i+1
        [2,1,5,4,3,0,0] 
           i i+1


        nothing can be greater than 5,4,3,0,0 
        but for this -> 1,5,4,3,0,0  -> 543100 can be greater next , but we want immediate next

        0.longest prefix match
        go from last n-2 to 1  not n-1 why?? atleast we need 2 to shuffle
        1. look for 1st break -> if i<i+1  1,5
        2. replace 1 by  5 or 4 or 3 , not 0,0 
        we want immediate next so 3
        [2,1,5,4,3,0,0] 
           i i+1
        [2,3,5,4,1,0,0] 
           i i+1

        3. after 3 we all small , so reverse it as 
        [2,1,5,4,3,0,0] -> [2,3,5,4,1,0,0] -> [2,3,0,0,1,4,5]

        4. edge case -> if [54321] i = -1 , next will be ver frist ie 12345 so just rev
        '''
        n = len(nums)
        index = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break

        if index ==-1:
            return nums.reverse()
        print(index,nums)
        for j in range(n-1,index,-1):
            if nums[j]> nums[index]:
                nums[index],nums[j] = nums[j],nums[index]
                break
                
        # print(nums[index+1:])
        nums[index+1:] = reversed(nums[index+1:])
        # nums[index+1:].reverse() ---> xxx as no changes in original , its just inplace 
        # nums = nums[:index+1] + nums[index+1:].reverse()
        return nums






        
        

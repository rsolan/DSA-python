https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n  = len(nums)
        # ans = n #--impppppppp
        # for i in range(n):
        #     ans = ans^i
        #     ans = ans^nums[i]

        # return ans

        # m2
        n = len(nums)
        nums.sort()
        print(nums)
        for ind,val in enumerate(nums):
            if ind!=val:
                return ind

        return n #- imp egde case

        ''' old
        # m0 - o(n2) - two for loops

        # m1 - o(n2) - ( for loops + sort) -> n +nlogn
        # nums.sort()
        # n = len(nums)
        
        # for i in range(n):
        #     if i!=nums[i]: --- tke help of index and not extra array
        #         return i

        # return n  #---imp edge case when last no is missing - 

        # Input: nums = [0,1]
        # Output: 2
        # Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.



        # m2 - optimal use of sum of n nos  -o(n) for sum

#         n = len(nums)
#         total = n * (n + 1) // 2
#         return total - sum(nums)


        # m3 - optimal - use of xor  - o(2n) - better as sum can be long int

        # x,y =0,0
        # n = len(nums)
        # for i in range(1,n+1):  #consider n also - edge case
        #     x= x^i
        
        # for i in nums:
        #     y = y^i
        
        # return x^y

        # m3' - optimal - use of xor  - o(n)
        
        n = len(nums)
        x = n #last no took first
        for i in range(0,n):  
            x= x^i
            x = x^ nums[i]
        
    
        return x
        '''

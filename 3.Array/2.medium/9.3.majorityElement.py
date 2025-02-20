https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0 #--imp start with 0
        el = nums[0]
        for i in range(n):
            if cnt ==0:
                cnt = 1 #now curr el - so start with 1
                el = nums[i]
            elif nums[i] ==el:
                cnt+=1
            else:
                cnt-=1

        return el

        '''
        # m1 - for each element - traverse the entire array to know the count , whichever elements count >n/2 is ans = 2 for loops O(N2)

        # M2 - O(N+D), SC - O(D)
        # d={}
        # for i in nums:
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i] =1
        # n = len(nums)
        # for i in d:
        #     if d[i] > n//2:
        #         return i 


        # M2 - MOORE'S VOTING ALGO , TC- O(2N) , SC- O(1)
        approach 2 : Boyer-Moore Voting Algorithm 
        This algorithm finds the majority element by maintaining a count, incrementing for the same element, and decrementing for different elements.
        nums = [2,2,1,1,1,2,2]
                1 2 1 0 1 0 1
        '''
        el = nums[0]
        cnt =0
        for i in range(len(nums)):
            if cnt ==0:
                cnt=1
                el = nums[i]
            elif nums[i] == el:
                cnt+=1
            else:
                cnt-=1
        # c=0 - these steps in case majority el not exist - not for this ques
        # n = len(nums)
        # for i in nums:
        #     if i == el:
        #         c+=1
        # if c>n//2:
        return el  #--- this will be th eonly el left as >n/2


        ''' sorting way approach 1
            nums.sort()
            return nums[len(nums) // 2]
        '''

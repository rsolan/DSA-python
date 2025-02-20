https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        d={}
        for ind,val in enumerate(nums):
            if target-val in d:
                return [d[target-val],ind]
            
            d[val] = ind   # 2:0




        # m1 - o(n2)
        # n = len(nums)
        # for i in range(0,n-1):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
            

        # m2 - dict  tc - o(n) , sc - o(n)   - better   
        # d={}
        # for i in range(len(nums)):
        #     rem = target - nums[i]
        #     if rem in d:
        #         return i, d[rem]

        #     d[nums[i]] = i
            
        # m3 - good for y/n ans- 2 pointer greedy approach , sort - but you have to store the indexes also 
        # n = len(nums)
        # nums.sort()
        # i =0
        # j = n-1
        # while i<j:
        #     if nums[i] + nums[j] == target:
        #         return [i,j]  #-- indx have changed now , good for y/n ans

        #     elif nums[i] +nums[j] > target:
        #         j-=1
        #     else:
        #         i+=1





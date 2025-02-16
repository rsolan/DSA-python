https://leetcode.com/problems/subsets-ii/description/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # no duplicates
        # wth dupicates - https://www.geeksforgeeks.org/problems/subset-sums2234/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=subset-sums

        # TC - 2^N SUBSET X N TIME TO APPEND DS TO ANS
        # SC - 2^N SUBSET WITH AVG LEN K -> 2^N x K
        # nums have to be sorted
        # start what can come at 0 index , then at 1st index
        #        ind
        # nums = [1,2,2,2,3,3]
        #             i

        # nums = [1,2,2]
        # subset - [],1,2,2,12,12,22,122 for n=3 , 8 subsets
        # without duplicates
        # subset - [],1,2,12,22,122
        
        def rec(ind,nums,ds,ans):
            
            ans.append(ds[:])

            for i in range(ind,n): #- no base case as lops run till n 
                if i!=ind and nums[i]==nums[i-1]:   #- remove duplicates f(2,ds=[2])
                    continue
                ds.append(nums[i])  # ds= 1,2,
                rec(i+1,nums,ds,ans)
                ds.pop()
                
        n = len(nums)
        nums.sort()
        ds=[]
        ans=[]
        rec(0,nums,ds,ans)
        return ans

https://leetcode.com/problems/k-diff-pairs-in-an-array/


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        #  m3 - optimla - o(nlogn) - 11345
        i = 0
        j = i+1
        nums.sort()
        # print(nums)
        n = len(nums)
        s1 = set()
        while j <n:
            if nums[j] - nums[i] == k:
                s1.add((nums[i],nums[j]))  #- imp to use set to store uniq pair
                # print(s1)
                i+=1
                j+=1
            elif nums[j] - nums[i] <k:
                j+=1
            else:
                i+=1
            if i==j:  #-- check if i and j are not at same index -- edge case imp
                j+=1

        return len(s1)



        # m2 - store pairs in set - o(n2)
        # imp -  pairs should be unique , pairs value can be same
        # s= nums
        # s.sort()
        # s1 = set()
        # n = len(s)
        # # print(n,s)
        
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if s[j]-s[i] == k:
        #             s1.add((s[i],s[j]))
                    
                    

        # return len(s1)

      


        # m1 - doesnt work for k =0 as pairs should be unique , pairs value can be same
        # s = list(set(nums))
        # s.sort()
        
        # n = len(s)
        # # print(n,s)
        # ans = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if s[j]-s[i] == k:
        #             ans+=1
        #             break

        # return ans
                     

https://leetcode.com/problems/longest-consecutive-sequence/submissions/1548972657/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # m1 - o(n2) - TLE
        # n = len(nums)
        # cnt =0
        # maxi = 0
        # sset = set(nums)
        # for i in nums:
        #     cnt = 1  #- start from 1
        #     while i+1 in sset:
        #         cnt+=1
        #         i+=1

        #     maxi = max(maxi,cnt)

        # return maxi

        # M2 - sort ->nlogn
        # nums.sort()
        # cnt = 1
        # maxi = 0
        # last_val = - float('inf')

        # for i in nums:
        #     if i-1 == last_val:  #1,2,3
        #         cnt+=1
        #         last_val = i
        #     # elif i== last_val: #1,1,2,3 , 100
        #     #     continue
        #     # elif i-1!= last_val: - checked in 1st st
        #     elif i!=last_val:
        #         cnt=1
        #         last_val = i

        #     maxi = max(maxi,cnt)

        # return maxi

        # m3 - optimal - o(n)
        # find the first occ only for 1234 -> we willonly count for 1 and not 234
        # so check for i if i-1 exist ->continue
        # if i-1 not exist -thats i is teh first letter -> then for this cehck if i+1...in set or not
        sset = set(nums)
        cnt = 1
        maxi = 1
        n = len(nums)
        if n == 0:
            return 0
        for i in sset: #--- traverse in set and not nummssss
            if i-1 not in sset:
                cnt = 1
                while i+1 in sset:
                    cnt+=1
                    i+=1      
            maxi  = max(maxi,cnt)

        return maxi

                











    
'''
        # m1 - bruteforce : check for i if i+1 exist or not and keep on inc the count for that : reset the count and return the max count
        # tc - o(n2) , sc = o(1) - 2 for loop

        # maxl = 1
        # s = set(nums)

        # for i in nums:
        #     c=1 #c = 1 as atleast 1 count for current el
        #     j = i+1
        #     while j in s:
        #         c+=1
        #         j+=1
        #     maxl = max(maxl,c)
        
        # return maxl



        # m3 - O(N + 2N)  - use set and if for i , i-1 exist - it means i is not starting point so skip this i
        # edce case - 0 LEN , no need to check if i-1 exist in set , main loop- check in set instead of nums 
        maxl = 1
        s = set(nums)
        n = len(nums)
        if n == 0:
            return 0
        for i in s:
            if i-1 not in s:
                c=1 #c = 1 as atleast 1 count for current el
                j = i+1
                while j in s:
                    c+=1
                    j+=1
                maxl = max(maxl,c)

            # else i is not the starting point
            
        return maxl




        # m2 - better - use sort
        # nums.sort()
        # n = len(nums)
        # if n ==0:
        #     return 0
        # cur =0
        # lastsmaller = float('-inf')
        # maxl=1
        # for i in range(n):
        #     if nums[i]-1 == lastsmaller:
        #         cur+=1
        #         lastsmaller = nums[i]
        #     elif nums[i] == lastsmaller:
        #         pass
        #     elif nums[i]!= lastsmaller:
        #         # seq broke
        #         cur = 1
        #         lastsmaller = nums[i]

        #     maxl = max(maxl,cur)
        # return maxl

'''
            

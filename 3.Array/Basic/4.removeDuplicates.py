https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j= i+1
        n = len(nums)
        cnt = 1 #- for first el  -->e dgc ase
        while j<n:
            if nums[j] == nums[i]:
                j+=1
            else:
                i=i+1
                nums[i],nums[j] = nums[j],nums[i]
                cnt+=1
                j+=1
        return cnt # or retrun i+1

        #            j
        # [0,1,0,1,1,2,2,3,3,4]
        #    i


        '''
        i  =0
        j = 1
        n = len(nums)
        while j<n:
            if nums[j]== nums[i]:
                j+=1
            else:
                i+=1
                nums[i] = nums[j]
                j+=1
        return i+1 #not index but count so retunr i+1




        # m1 - use sets , list sort , iterate l --

        # tc - nlogn +n , sc - o(n) extra set space
        # s = set(nums) 
        # l = list(s)
        # l.sort()
        # print(l,s)
        # k = len(s)
        # for i in range(len(l)):
        #     nums[i] = l[i]
        # print(nums)
        # return k

# doesnt work with negative nos , so sort the list
# nums = [-1,0,0,0,0,3,3]
# Stdout
# l = [0, 3, -1] s= {0, 3, -1}
# [0, 3, -1, 0, 0, 3, 3]



# m2 - OPTIMAL - 2 pointer approach tc - o(n) , sc - o(1)

        i = 0
        if len(nums) < 2:
            return 1
        n = len(nums)
        for j in range(1,n):  #use for loop instead of while loop
            if nums[i]!= nums[j]:
                nums[i+1] = nums[j]
                i+=1

        return i +1
        '''    

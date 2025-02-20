https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # DNF ALGO
        l = 0
        m = 0
        n = len(nums)
        h = n-1

        # l              h
        # [2,0,2,1,0,1,1,0]
        # m

        #      l       h
        # [0,0,2,1,0,0,1,2]
        #      m

        #      l     h
        # [0,0,1,1,0,0,2,2]
        #          m

        #        l   h
        # [0,0,0,1,1,0,2,2]
        #            m

        #          l h
        # [0,0,0,0,1,1,2,2]
        #              m

        while m<=h:
            if nums[m] ==0:
                nums[l],nums[m] = nums[m],nums[l]
                l+=1
                m+=1
            
            elif nums[m] ==1:
                m+=1

            else:
                nums[m],nums[h]= nums[h],nums[m]
                h-=1







        '''

        # m1 - o(n+n)
        # count0 = 0
        # count1 = 0
        # count2 = 0
        # n = len(nums)
        # for i in nums:
        #     if i==0:
        #         count0+=1
        #     if i==1:
        #         count1+=1
        #     if i ==2:
        #         count2+=1

       
        # for i in range(0,count0):
        #         nums[i] = 0
        # for i in range(count0,count0+count1):
        #         nums[i] = 1
            
        # for i in range(count0+count1,n):
        #         nums[i] = 2

        # m2 - DNF ALGO - O(N)
        l= 0
        m=0
        n = len(nums)
        h = n-1
        # last low at first 1 , medium continues , high at 2
        while m<=h:
            if nums[m] == 0:
                nums[m],nums[l] = nums[l],nums[m]
                l+=1
                m+=1
            elif nums[m] == 1:
                m+=1
            else:
                nums[m],nums[h] = nums[h],nums[m]
                h-=1

        '''


        

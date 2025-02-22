https://leetcode.com/problems/valid-triangle-number/


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # strcitly 
        # a+b>c
        # a+c>b
        # c+b>a

        # 2 3 4 4
        #               i
        # # 1 2 2 2 4 6 8 8 9 9  9 14 15 17
        #                        j        k
        # a<b<c

        # o(n2)
        nums.sort() #--imp so have to check 1 case instead of 3
        n = len(nums)
        ans = 0
        for k in range(n-1,-1,-1):
            i = 0
            j = k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    ans = ans+(j-i) 
                    j-=1
                else:
                    i+=1
            
        return ans


                


                      









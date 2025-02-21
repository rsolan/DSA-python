https://leetcode.com/problems/4sum/submissions/1551189263/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # m3 - o(nlohn)+o(n2)
        nums.sort()
        n = len(nums)
        ans =[] #no set as arr sorted
        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,-1,0,1,2]
        for i in range(n) :
            if i>0 and nums[i]==nums[i-1]:continue #--imp cond

            for j in range(i + 1, n):
                if j>i+1 and nums[j]== nums[j-1]:continue  #orj>i+1
                k = j+1
                l = n-1
                while k<l:
                    total_sum = nums[i] + nums[j] + nums[k]+nums[l]
                    if total_sum <target:   #target not 0
                        k+=1
                    
                    elif total_sum>target:
                        l-=1
                    else:
                        temp = [nums[i], nums[j], nums[k],nums[l]]
                        ans.append(temp)
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:k+=1   #---imp to move till , also check j<k
                        while k<l and nums[l] == nums[l+1]:l-=1

        return ans

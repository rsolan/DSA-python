https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # m3 - o(nlohn)+o(n2)
        nums.sort()
        n = len(nums)
        ans =[] #no set as arr sorted
        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,-1,0,1,2]
        for i in range(n) :
            if i!=0 and nums[i]==nums[i-1]:continue #--imp cond
            j = i+1
            k = n-1
            while j<k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum <0:
                    j+=1
                
                elif total_sum>0:
                    k-=1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:j+=1   #---imp to move till , also check j<k
                    while j<k and nums[k] == nums[k+1]:k-=1

        return ans





        

        '''

        # m2 - n2 but extra space
        d={}

        out = set()
        n = len(nums)
        # [-1,0,1,2,-1,-4] , d= 0,1,2
        #  i         j
        for i in range(n):
            d={} #--imp step
            for j in range(i+1,n):
                rem= -(nums[i]+nums[j])
                if rem in d:
                        temp = [nums[i], nums[j],rem]
                        temp.sort()  #- IF WE ARE sorting th main array, dont do this
                        out.add(tuple(temp))
                d[nums[j]] = j
        return list(out)



        # m1 - o(n3) TLE
        # nums.sort()
        out = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()  #- IF WE ARE sorting th main array, dont do this
                        out.add(tuple(temp))
        return list(out)

        '''

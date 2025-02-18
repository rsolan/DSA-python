https://leetcode.com/problems/contiguous-array/description/


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # binary array
        # 1001
        # [ 0, 1, 0, 0, 0, 1, 1, 0, 1]
        # [-1  0 -1 -2 -3 -2 -1 -2 -1]
        #   1 1 2 3 4 4 4 5 5
        #   to reach -2 to -2 : the count of adds/subs must compensate ->store 1st index
        #   0 -

        ps =[]
        c =0
        for i in nums:
            if i==0:
                c-=1
            else:
                c+=1
            ps.append(c) 
    #  [0      2 ]
    # [ 0, 1, 0, 0, 0, 1, 1, 0, 1]
    # [-1  0 -1 -2 -3 -2 -1 -2 -1]
        d={}
        d[0] = -1
        n = len(nums)
        maxi = 0
        # for ind in range(n):
        #     if ps[ind] in d:
        #         maxi = max(maxi,ind-d[ps[ind]])
        #     else:
        #         d[ps[ind]] = ind  # -1 : 0   val:ind
        
        for ind,val in enumerate(ps):
            if val in d:
                maxi = max(maxi,ind-d[val])
            else:
                d[val] = ind  # -1 : 0   val:ind

        return maxi


        






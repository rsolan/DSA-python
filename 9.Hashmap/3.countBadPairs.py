https://leetcode.com/problems/count-number-of-bad-pairs/

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # brutforce - o(n2)

        # total - good pairs
        # j - i == nums[j] - nums[i].
        d ={}
        n = len(nums)
        for i in range(n):
            if nums[i] - i in d:
                d[nums[i] - i]+=1
            else:
                d[nums[i] - i] = 1

        # print(d)
        gp =0
        for i in d:
            v = (d[i]*(d[i]-1))//2
            # print(v,gp)
            gp = gp + v
        # print(gp)

        tp = (n*(n-1))//2
        # print(tp)
        return tp-gp


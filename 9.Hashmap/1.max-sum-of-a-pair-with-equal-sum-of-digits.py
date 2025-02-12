https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # 164
        # 1. precompute
        d={}
        for i in nums:
            sumj =0
            no = i
            while no:
                c = no%10
                sumj = sumj + c
                no = no//10
            if sumj in d:
                d[sumj].append(i)
            else:
                d[sumj] = [i]  #--init as list

        print(d)
        
        maxsum = 0
        for i in d:
            maxi = 0
            smaxi =0
            if len(d[i])>1:
                for j in d[i]:
                    if j>maxi:
                        smaxi = maxi
                        maxi = j   
                    elif j>smaxi and j<=maxi: #-- handle duplicates 
                        smaxi = j
                print(i,j, maxi,smaxi)
                maxsum = max(maxsum,maxi+smaxi)

        if maxsum ==0: #-- imp take
            return -1
        return maxsum





3) PRINT ALL WHOSE SUM = K
https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        '''
        # tc - exponential - 2^t x k
        sc - k avg len  x X comb
        # index - can b pick multiple time / not pic at all
        [2,3,6,7]
        2+2+2+2 - > target <0 -> return 
        2+2+3 --> target =0 saved and return
'''
        def rec(ind,arr,ds,target,out):
            if ind == n:   #-- whyy check n
                if target == 0:
                    out.append(ds[:])
                return

            # if arr[ind]>target: #- can never be my ans  2,2,2 target left = 1 , next arr = 2 
            #     return

            if arr[ind]<= target:        #- like a lop
                ds.append(arr[ind])
                rec(ind,arr,ds,target-arr[ind],out)  #- picked -so pick again,ind not moved picked so sub targte
                ds.pop()

            rec(ind+1,arr,ds,target,out) #- not picked , move to next , no chang in targt

        n = len(arr)
        out = []
        ds = []
        rec(0,arr,ds,target,out)
        return out


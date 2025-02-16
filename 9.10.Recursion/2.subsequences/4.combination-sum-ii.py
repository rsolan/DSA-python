https://leetcode.com/problems/combination-sum-ii/


class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        '''
        pick and non pick only , no multiople pic
        tc - 2^n x k  . k is avg len of each subsw
        sc - k len x Xcombinations
        since unique comb - taek set

        '''
        # m2 - 
        def rec(ind,arr,ds,target,out):
            if target ==0:
                out.append(ds[:])
                return #- imp

            for i in range(ind,n):  #- not start with ind+1
                if i > ind and arr[i]== arr[i-1]:   # or if i!= ind and arr[i]== arr[i-1]:
                    continue
                if arr[i]>target:
                    break  # - can never be ans for that ind
                ds.append(arr[i])
                rec(i+1,arr,ds,target-arr[i],out)
                ds.pop()


        arr.sort()
        n = len(arr)
        out = []
        ds = []
        rec(0,arr,ds,target,out)
        return out


        ''' - now working , tc - 2^n x klogk
        # m1 - if use set and comb sum 1 part
        def rec(ind,arr,ds,target,out):
            if ind == n:   #-- whyy check n
                if target == 0:
                    out.add(ds[:])
                return

            # if arr[ind]>target: #- can never be my ans  2,2,2 target left = 1 , next arr = 2 
            #     return

            if arr[ind]<= target:        #- like a lop
                ds.append(arr[ind])
                rec(ind+1,arr,ds,target-arr[ind],out)  #- picked -so pick again,ind not moved picked so sub targte
                ds.pop()

            rec(ind+1,arr,ds,target,out) #- not picked , move to next , no chang in targt

        n = len(arr)
        out = set()
        ds = []
        rec(0,arr,ds,target,out)
        return out
        '''

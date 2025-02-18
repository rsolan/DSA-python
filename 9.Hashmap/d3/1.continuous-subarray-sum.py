https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        #  presum -nk
        s =0
        pf =[]
        for i in nums:
            s=s+i
            pf.append(s)

        rem =[]
        for i in pf:
            rem.append(i%k)
        
        print(pf,rem)
        d={}
        d[0] = -1  #we are adding one mroe freq of 0 , so zero repeats that ans
        n = len(nums)
        for ind in range(n):
            if rem[ind] in d:
                # return True  #- check len>2
                if ind - d[rem[ind]] >=2:
                    return True
                # else:
                #     return False  as there can be other cases also 
            else:
                d[rem[ind]] = ind   # 5 :0  val:ind
            # print(d)
            


        # print(d)
        return False


'''
        nums = [23, 2, 4, 6, 7]

        pref=  [23,25,29,35,42]
               [5, 1, 5, 5, 0]  - rem

               2, 4, 6,
               2, 4
               23, 2, 4, 6, 7

               if 2 el same rem 
               23%k = 5
               29%k = 5
               so dif - 29-23 = 6 as 29 has to be inc by nk (mult of 6) to give same rem
               sub array wil lb e mult of k

'''














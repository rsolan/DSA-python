https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # TC - n!xn
        # SC - n!  ->NO EXTRA SPACE
        # m2
        # we try all el at 0th index - use swap -> not estart from 0th index not from ind+1
        #  123 -> 123 , 213, 321
                #  123    213  321
                #  132    231  312
        def rec(ind,nums,out):
            if ind ==n: #-- adding at wehn ind crooses n
                out.append(nums[:]) #---vvvimp as nums keep on changing
                return

            for i in range(ind,n):
                nums[ind],nums[i] =  nums[i],nums[ind]
                rec(ind+1,nums,out) #--- ind moves not i
                nums[ind],nums[i] =  nums[i],nums[ind]

        n = len(nums)
        out = []
        rec(0,nums,out)
        return out

        '''
        # m1
        for n numbers - > n! permutaions possible
        TC - n!xn
        SC - n!x n ds + n map
        [1,2,3]
         1 can be at first index - > 2nd index - 2 or 3  --. (1,2) and (1,3)  --> (1,2,3) and (1,3,2)
         2  
         3 

         so keep a note fo already visited - dict

        

        # def rec(nums,d,ds,out):
        #     if len(ds) ==n:     #---vvimppp , # NO INDEX -> ind == n , what ind?
        #         out.append(ds[:])
        #         return

        #     for i in range(0,n): ##- not from ind as we can take anything which not taken before(USE DICT to map)
        #         if i not in d:
        #             ds.append(nums[i])
        #             d[i]=1
        #             rec(nums,d,ds,out)
        #             del d[i] #- or initialzie with 0 and then make it 0
        #             ds.pop()


        # n = len(nums)
        # d={}
        # out = []
        # ds =[]
        # rec(nums,d,ds,out)

        # return out


        def rec(nums,d,ds,out):
            if len(ds) ==n:     #---vvimppp , # NO INDEX -> ind == n , what ind?
                out.append(ds[:])
                return

            for i in range(0,n): ##- not from ind as we can take anything which not taken before(USE DICT to map)
                if d[i]==0:
                    ds.append(nums[i])
                    d[i]=1
                    rec(nums,d,ds,out)
                    d[i]=0 #- or initialzie with 0 and then make it 0
                    ds.pop()


        n = len(nums)
        # d={0 for _ in range(n)} ->notworked
        # d = {0}*n ->not worked
        d={}
        for i in range(n):
            d[i]=0
        out = []
        ds =[]
        rec(nums,d,ds,out)

        return out

        '''


        



https://leetcode.com/problems/permutations-ii/description/
https://leetcode.com/problems/permutation-in-string/   ----------------------do this

https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        x=0
        for i in nums:
            x=x^i

        return x
        '''


# m1 - brute force - o(n2)  = 2 for loops for linear search and inc the counter , return i where i count is 1
# m2 - better - hashing/dict , return whose hash value is 1 insetad of 2 , but whtas the size of hash array - max ele of nums tc - o(3n) , sc - o(n)

        d={}
        n = len(nums)
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] =1

        # print(d)
        for i in d:
            if d[i] ==1:
                return i
# m3 - optimal - use xor

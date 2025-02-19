https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # even-odd any length - https://www.naukri.com/code360/problems/alternate-numbers_6783445?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems
        # even length

        # m1 - bruteforce , tc - o(n+n/2) sc - o(n)
        '''
        n  = len(nums)
        pos=[]
        neg=[]

        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i) #no zereos
        ans=[0]*n  #--imp to initialze
        for i in range(n//2):
            ans[2*i] =pos[i]  #0,2,4
            ans[2*i+1] = neg[i] #1,3,5

        return ans
        '''

        # m2 - 1 pas - tc = o(n)
        # all pos el will come on even indx
        # neg el on odd index of ans 
        n = len(nums)
        ans =[0]*n
        pos = 0
        neg = 1
        for ind,val in enumerate(nums):
            if val>0:
                ans[pos] = val
                pos+=2
            else:
                ans[neg] = val
                neg+=2
        return ans


====
from typing import *

def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    # n = can be even odd
    n = len(a)
    pos=[]
    neg=[]

    for i in a:
        if i>0:
            pos.append(i)
        else:
            neg.append(i)

    p = len(pos)
    ne = len(neg)
    ans = [0]*n
    # neg = [-2,-5,-4,-6,-8,-9]
    # pos = 312

    if p<ne:
        for i in range(p):
            ans[2*i] = pos[i]
            ans[2*i+1] = neg[i]

        for i in range(p,ne): #---vvimp from pos len to neg len
            ans[2*i] = neg[i]

    else:
        for i in range(ne):
            ans[2*i] = pos[i]
            ans[2*i+1] = neg[i]

        for i in range(ne,p): #-- from neg len to poslen
            ans[2*i] = pos[i]

    return ans

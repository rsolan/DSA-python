preprocess k window
maxi = old ans
include and exclude


https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = 'aeiou'
        cnt  =0 
        n  = len(s)
        for i in range(k):
            if s[i] in v:
                cnt+=1

        include = k
        exclude = 0
        maxi = cnt

        while include<n:
            if s[include] in v:
                cnt+=1
            if s[exclude] in v:
                cnt-=1

            maxi = max(maxi,cnt)

            include+=1
            exclude+=1

        return maxi

        '''

        # m1- bruteforce -TLE
        # n = len(s)
        # v= 'aeiou'
        # maxi = -float('inf')
        # for i in range(n-k+1):
        #     cnt =0
        #     for j in range(i,i+k):
        #         if s[j] in v:
        #             cnt+=1
        #     maxi = max(maxi,cnt)
        # return maxi



        # m2 - fixed window

        # step1 - preprocess
        n  = len(s)
        v= 'aeiou'
        cnt =0
        for i in range(k):
            if s[i] in v:
                cnt+=1
        
        maxi = cnt #- STORE COUNT OF FIRST WINDOW
        inc= k
        exc = 0
        while inc!=n:
            if s[inc] in v:
                cnt+=1
            if s[exc] in v:
                cnt-=1

            maxi = max(maxi,cnt)
            inc+=1
            exc+=1

        return maxi

        '''

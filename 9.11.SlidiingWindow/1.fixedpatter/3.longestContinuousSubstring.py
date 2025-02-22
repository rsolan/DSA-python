https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        cnt = 1
        n = len(s)
        maxi = 1
        for i in range(n-1):
            if ord(s[i+1]) - ord(s[i]) == 1:
                cnt+=1
            else:
                cnt = 1

            maxi = max(maxi,cnt)

        return maxi
        '''

        # M1- TAKE HELP OF ORDER - as consecutive char will have diff of 1 
        
        cnt = 1  #-- start from cnt 1 as current char u r stadning should also be taken 
        maxi = - float('inf')
        for i in range(len(s)-1):  #- not the last index 
            if ord(s[i+1]) - ord(s[i]) ==1:
                cnt+=1
            else:
                maxi = max(maxi,cnt)
                cnt = 1 #-- start from cnt 1 
        maxi = max(maxi,cnt)

        return maxi
        '''

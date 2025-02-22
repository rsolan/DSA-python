https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se =set()
        n = len(s)
        left = 0
        right = 0
        maxi = 0
        for right in range(n):
            while s[right] in se:
                se.remove(s[left])
                left+=1

            se.add(s[right])
            maxi = max(maxi,right-left+1)

        return maxi
        '''
        # m1 - bruteforce - n2

        # n = len(s)
        # if n ==0:   # --edge case1 
        #     return 0
        # if s == " ":  #- edge case2
        #     return 1

        # maxi = -float('inf')
        # for i in range(n):
        #     d={}
        #     cnt =0
        #     for j in range(i,n):
        #         if s[j] in d:
        #             # maxi = max(maxi,cnt)
        #             break 
        #         else:
        #             d[s[j]] = 1
        #             cnt+=1
        #         maxi = max(maxi,cnt)

        # return maxi


        # m2 - SLIDING WINDOW
        n = len(s)
        se = set()
        left =0
        maxi = 0
        cnt=0
        
        for right in range(n):
            while s[right] in se:
                se.remove(s[left])
                left+=1
                cnt-=1
            
            se.add(s[right])
            cnt+=1
            # maxi = max(maxi,right-left+1)   #-- without using cnt var lenght = r-l+1
            maxi = max(maxi,cnt)

        return maxi

        '''












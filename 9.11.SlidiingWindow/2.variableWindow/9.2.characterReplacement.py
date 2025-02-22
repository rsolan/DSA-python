https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # o(26*n) - O(N)
        # p = is my prioirty char  tht i can take 

        def slide(p):
            left =0
            n = len(s)
            cnt = 0
            maxi = 0
            for right in range(n):
                if s[right] != p: #--- imp not ==
                    cnt+=1  #inc the count when its not p , so its violation
                
                
                while cnt>k:
                    if s[left] != p:
                        cnt-=1  #reduce violations
                    left+=1
                maxi = max(maxi, right-left+1)

            return maxi

        maxx= 0
        se = set(s)  #- instead of trying all 26 letetrs , just try those in s
        for i in se:
             maxx =  max(maxx, slide(i))
            
        return maxx

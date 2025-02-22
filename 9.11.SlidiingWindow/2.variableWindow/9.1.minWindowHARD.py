https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def fun(d1,d2):
            # check if d1 is subset of d2-> all char of t should be in s , with = or more freq
            for i in d1:
                if i in d2:
                    if d1[i] > d2[i]:   #s = "a", t = "aa"
                        return False
                else:
                    return False
            return True


        ind = -1
        mini = float('inf')
        d1={}
        m = len(s)
        n = len(t)
        for i in range(n):
            if t[i] in d1:
                d1[t[i]]+=1
            else:
                d1[t[i]] = 1

        left = 0
        d2={}
        for right in range(m):
            if s[right] in d2: #1
                d2[s[right]]+=1
            else:
                d2[s[right]] = 1

            # print(left, right, d2)
            while fun(d1,d2):     
                if mini > (right-left+1):  #=== strping inside while loop #3
                    mini = right-left+1
                    ind = left
                # print(mini,right,left , ind)
                d2[s[left]]-=1   #zzADOBECOD  #2 inside pnly
                left+=1


        # print(ind,mini)
        if mini == float('inf'):
            return ""
        return s[ind:ind+mini]

                
                

            

# AABC
# ABBC
# ABCC

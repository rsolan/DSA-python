https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        d = {}
        n = len(s)
        m = len(p)

        out =[]
        if m>n: #-- edgecase
            return out
        for i in p:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        d1={}
        for i in range(m):
            if s[i] in d1:
                d1[s[i]]+=1
            else:
                d1[s[i]]=1


        inc = m
        exl=0

        while inc<n:
            if d==d1:  #as we havent check preprocesed ans = k win
                out.append(exl)
            
            if s[inc] in d1:
                d1[s[inc]]+=1
            else:
                d1[s[inc]]=1

            d1[s[exl]]-=1
            if d1[s[exl]]==0:
                del d1[s[exl]]

            inc+=1
            exl+=1
            
                
        if d==d1:
            out.append(exl)

        return out

        '''
        # ANAGRAMS - USING SORTING OR TOTAL OCC
        # m2 - 
        n = len(s)
        k = len(p)

        if k > n :  #-- base case - imp
            return []

        out =[]
        d={}
        for i in p:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        
        
        d1={}
        # step1 - preproces for k size
        for i in range(k):
            if s[i] in d1:
                d1[s[i]]+=1
            else:
                d1[s[i]] =1
        
        inc=k
        exc=0
        # step2 - slide window till inc out of arr
        while inc!=n:
            if d==d1:
                out.append(exc)
            
            if s[inc] in d1:
                d1[s[inc]]+=1
            else:
                d1[s[inc]] =1
            
            
            d1[s[exc]]-=1
            
            if d1[s[exc]] == 0:  #when any value becomes 0 - delete it -- imp (prevent issue in comparison)
                del d1[s[exc]]

            inc+=1
            exc+=1

        if d==d1:  #- since checking first - so last one is left
                out.append(exc)
        return out
        


        # m1 - bruteforce - TLE 
        # out =[]
        # d={}
        # for i in p:
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i]=1
        
        # n = len(s)
        # m = len(p)
        # d1={}
        # for i in range(n-m+1):
        #     d1={}
        #     for j in range(i,i+m):
        #         if s[j] in d1:
        #             d1[s[j]]+=1
        #         else:
        #             d1[s[j]]=1
            
        #     if d==d1:
        #         out.append(i)

        # return out
        '''



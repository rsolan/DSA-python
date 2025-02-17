https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # counting char
        # sort 


        # strs = ["eat","tea","tan","ate","nat","bat"]
        #          aet   aet         aet
        # eat,aet

        d={}

        # i.sort()
        # o = sorted(strs)
        # print(o)
        for i in strs:
            p= sorted(i)
            s = "".join(p) #--imp step 
            # print(s,i)
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i] #- imp list

        print(d)

        out=[]
        for i in d:
            out.append(d[i])

        return out






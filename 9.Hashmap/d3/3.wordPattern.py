https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, p: str, s: str) -> bool:

        # No two letters map to the same word (2), and no two words map to the same letter(1).
        # print(lis)
        # lis = ['dog', 'cat', 'cat', 'fish' , 'dog']
        # p = "abbaz"
        # d = {a:dog, b: cat , }


        d={}
        lis = s.split()
        Set =set()
        if len(lis)!= len(p):  #-------imp edge case
            return False
        for ind,val in enumerate(p):
            if val in d  :
                # no issu if they are equal -> b:Cat
                if d[val] != lis[ind]:  #-> 1. if a:dog, a:fish   ; a already exist but dog!=fish
                    return False
            else:
                # 2. return false if new el that has to be added z belongs to dog , but dog already has index a
                if lis[ind] in Set:
                    return False
                d[val] = lis[ind]
                Set.add(lis[ind])

            print(d,Set)


        return True

        # 



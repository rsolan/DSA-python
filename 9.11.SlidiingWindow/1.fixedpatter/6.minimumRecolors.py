https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/submissions/1551316668/

class Solution:
    def minimumRecolors(self, bl: str, k: int) -> int:

        n = len(bl)
        c=0
        for i in range(k):
            if bl[i] == 'W':
                c+=1

        inc = k
        exc = 0
        mini = c
        while inc<n:
            if bl[inc]=='W':
                c+=1
            
            if bl[exc] == 'W':
                c-=1

            mini = min(mini,c)
            inc+=1
            exc+=1

        return mini

        '''


        cnt = 0
        for i in range(k):
            if blocks[i] == 'W':
                cnt+=1
        n = len(blocks)
        inc = k
        exc =0

        mini = cnt
        while inc!=n:
            if blocks[inc]=='W':
                cnt+=1
            if blocks[exc] == 'W':
                cnt-=1

            mini = min(mini,cnt)
            inc+=1
            exc+=1

        return mini

        '''

        


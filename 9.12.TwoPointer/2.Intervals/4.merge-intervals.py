https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, inv: List[List[int]]) -> List[List[int]]:
        # m1 - bruteforce - o(n2) xxx
        # tc - nlogn + 2n  -> 2 pas
        # [1,3],[2,4],[2,6],[8,9],[8,10],[15,18],[16,17]]

        # inv.sort()
        # n = len(inv)
        # ans = []
        # for i in range(n):
        #     s = inv[i][0]
        #     e = inv[i][1]
        #     if ans and e<=ans[-1][1]: #ans ahs 1,6 -> so j wont move for 2,4
        #         continue
        #     for j in range(i+1,n):
        #         if inv[j][0]<=e:
        #             e = max(e,inv[j][1])  #update end 
        #         else:
        #             break

        #     ans.append([s,e]) #s remain same ,end chanegs

        # return ans



        #  m2 - do in 1 pas - nlogn+n
        # [1,3],[2,4],[2,6],[8,9],[8,10],[15,18],[16,17]]
        # if - push an intrval if not overlapping ans = 1,6     , inv = [8,9] 
        # else - update teh ans -> ans = [1,3]    , inv = [2,4]

        inv.sort()
        n = len(inv)
        ans = []
        for i in range(n):
            if not ans or inv[i][0]> ans[-1][1]: #8>6 , if an sempty just push 1,3
                ans.append(inv[i])
            else: #2!>3
                ans[-1][1] = max(ans[-1][1],inv[i][1])  #max (3,4)

        return ans



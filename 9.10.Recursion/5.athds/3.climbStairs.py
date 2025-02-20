https://leetcode.com/problems/climbing-stairs/description/


class Solution:
    def climbStairs(self, n: int) -> int:
        # fibo nac
        # reach n -> n-1 and n-2
        # 3 - > 1 + 2

        # 2-> 
# 0 to 1 - > 1 step
# 0 to 2 -> 1 step
        memo ={}

        def rec(n):
            if n ==0:
                return 1 #- to reach 0 ist 1 way
            if n ==1:
                return 1
            # if n == 2:
            #     return 2

            if n in memo:
                return memo[n]

            memo[n] = rec(n-1) + rec(n-2)
            return memo[n]

        return rec(n)

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



# 27TH DEC


class Solution:
    # def climbStairs(self, n: int) -> int:
    #     # n -> n -1 + n-2

    #     def rec(n):
    #         if n <=1 :
    #             return 1
    #         return rec(n-1) + rec(n-2)


    #     return rec(n)


    # def climbStairs(self, n: int) -> int:
    #     dp={}

    #     def rec(n):
    #         if n <=1 :
    #             return 1
    #         if n in dp:
    #             return dp[n]
    #         dp[n]= rec(n-1) + rec(n-2)
    #         return dp[n]


        # return rec(n)




    # def climbStairs(self, n: int) -> int:
    #     dp={}

    #     def rec(n):
    #         if n <=1 :
    #             return 1
    #         dp = [0]*(n+1)
    #         dp[0],dp[1] = 1,1

    #         for i in range(2,n+1):
    #             dp[i] = dp[i-1]+dp[i-2]
            
    #         return dp[n]


    #     return rec(n)

    # NOT WORK AS THESE ARE WAYS 
    def climbStairs(self, n: int) -> int:
        
        def rec(n):
            if n <=1 :
                return 1
            a,b = 1,1

            for i in range(2,n+1):
                a,b = a,a+b
            
            return b


        return rec(n)
        

https://leetcode.com/problems/n-th-tribonacci-number/description/


class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def rec(n):
            if n == 0:
                return 0
            if n==1 or n ==2:
                return 1
            if n in memo:
                return memo[n]

            # return rec(n-1)+rec(n-2)+rec(n-3) #exponential time complexity of O(3ⁿ).
            memo[n] = rec(n-1)+rec(n-2)+rec(n-3)  #- store the ans
            return memo[n]

        return rec(n)
'''
# USE OF DP
Approach 1: Memoization (Top-Down)
We use a cache (dictionary or list) to store previously computed values.
Time Complexity: O(N) (Each value is computed once and stored).
Space Complexity: O(N) (For recursion stack and memoization storage).
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def rec(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n in memo:
                return memo[n]  # Return stored value
            
            # Compute and store the result
            memo[n] = rec(n-1) + rec(n-2) + rec(n-3)
            return memo[n]

        return rec(n)

Approach 2: Tabulation (Bottom-Up)
Instead of recursion, we build up the solution iteratively.
We use an array dp where dp[i] stores T(i).
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 1
        
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[n]

Approach 3: Space-Optimized DP (Constant Space)
Since T(n) depends only on the last three values, we don't need a full array.
We store only the last three computed values and update them iteratively.
Time Complexity: O(N).
Space Complexity: O(1).
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c  # Move the window forward

        return c
'''

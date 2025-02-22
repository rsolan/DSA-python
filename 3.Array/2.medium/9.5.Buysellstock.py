https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        ans  = 0
        maxprofit  =0
        # go from n-1 to 1
        # buy at current index , sel at max after that point - so better to go from n to 1
        n = len(prices)
        for ind in range(n-1,-1,-1):
            maxi = max(maxi,prices[ind]) #max profit from n -> 6
            maxprofit = max(maxprofit,maxi - prices[ind])  # 6 - current index -> 6-1 = 5

        return maxprofit




        # for every i 
        # find min from 0 to i-1
        # return max profit


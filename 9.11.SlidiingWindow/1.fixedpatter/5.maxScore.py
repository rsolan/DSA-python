https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, c: List[int], k: int) -> int:
        n = len(c)

        s =0
        for i in range(k):
            s=s+c[i]
        maxi = s
        inc = n-1
        exc= k-1  #3---imp as we have to remove k-1  , NOT K

        while exc>=0:
            s=s+c[inc]-c[exc]
            maxi = max(maxi,s)
            inc-=1
            exc-=1

        return maxi


        '''
        n = len(cardPoints)
        exc = k-1  #-- start from k-1 and not k 
        inc = n-1
        # k = 3

        #                   k
        # cardPoints = [1,2,3,4,5,6,1]
        sumj =0
        for i in range(k):
            sumj+=cardPoints[i] #1+2+3

        maxi = sumj
        while exc>=0:
            sumj = sumj - cardPoints[exc] + cardPoints[inc] #rem 3 add 1
            #                 e         i
            # cardPoints = [1,2,3,4,5,6,1]

            exc-=1
            inc-=1
            maxi = max(maxi,sumj)

        return maxi
        '''

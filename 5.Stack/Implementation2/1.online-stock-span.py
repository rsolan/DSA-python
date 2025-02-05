# https://leetcode.com/problems/sliding-window-maximum/description/

# m2 - 
class StockSpanner:

    def __init__(self):
        self.ind=-1
        self.st =[]

    def next(self, price: int) -> int:
        # pgee from 0 to n 
        self.ind = self.ind+1
        while self.st and self.st[-1][1] <= price:   #- equal as PGEE
            self.st.pop()
            
        if self.st:
            ans = self.ind - self.st[-1][0]
        else:
            # ans = 1
            ans = self.ind - (-1)

        self.st.append((self.ind,price))
        return ans
        


'''
# m1 - bruteforce - TLE
class StockSpanner:

    def __init__(self):
        self.res=[]

    def next(self, price: int) -> int:
        self.res.append(price)
        cnt = 1
        n = len(self.res)
        for i in range(n-2,-1,-1):
            if self.res[i] <= price:
                cnt+=1
            else:
                break
        return cnt
'''

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# store pge and equal PGEE ele - but we can only move forward so use striver approach, to strt from 0 to n
# store pgee and inde
# why to celar stack for each itr

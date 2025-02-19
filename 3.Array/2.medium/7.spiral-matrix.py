https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, a: List[List[int]]) -> List[int]:
        #  tc - nm , sc - nm
        n = len(a)
        m = len(a[0])
        top = 0
        bot = n-1  #- imp to have n-1,m-1 and NOT n,m
        left = 0
        right = m-1
        out =[]

        # left->
        # top             <-right
        #     |
        #    \/

        #     ^
        #     |
        # bot

        # order -  1to4 , 8 to 12 , 11 to 9 , 5to 
        #  right bottom  left top

        while top<=bot and left<=right:  # total check

            for i in range(left,right+1):  #-- inc right
                out.append(a[top][i])
            top+=1

            for i in range(top,bot+1): #- inc bot
                out.append(a[i][right])
            right-=1

            if top<=bot:   #-- check 1
                for i in range(right,left-1,-1):  #- inc left so go til left
                    out.append(a[bot][i])
                bot-=1

            if left<=right: #-- check 2
                for i in range(bot,top-1,-1):  # same inc top
                    out.append(a[i][left])
                left+=1
            
        # print(out)
        return out



            

# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # M3 - OPTIMIZED IN 1 PASS - know nse and pse
        # stack - in monoton inc order
        # if dec comes - calc area for top of stack 
        # for top of stack - nse - current el
        # pse - prev el in stack

        # h = [3 2 10 11 5 10 6 3]
        # tc - o(n)traversal + o(n) while st pop  , sc- o(n)
        n = len(heights)
        st =[]
        maxi = 0
        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                top = st.pop()
                nse = i
                if st:
                    pse = st[-1]
                else:
                    pse = -1
                maxi = max(maxi,heights[top] * (nse-pse-1) )
                #for 11 area=h*w = 11 *(nse-pse-1)=11*(i*st[-1]) = 11(5index * 10index)
                
            st.append(i) #- store index

        # 2 edeg case -> 2 doesnt have pse so - 1, for 2,3 no nse - so n
        # stack has remaining el - 2 3
        while st:
            top = st.pop()
            nse = n
            if st:
                pse = st[-1]
            else:
                pse = -1
            maxi = max(maxi,heights[top] * (nse-pse-1) )
        return maxi


        '''
        # m1 - bruteforce -TLE
        n = len(heights)
        maxi = 0
        for i in range(n):
            nse = 1
            for j in range(i+1,n):
                if heights[i] <= heights[j]:
                    nse+=1
                else:
                    break
             

            pse = 0
            for j in range(i-1,-1,-1):
                if heights[i] <= heights[j]:
                    pse +=1
                else:
                    break
            h = heights[i]
            w = nse+pse
            # print(nse,pse)
            maxi = max(maxi,h*w)
        return maxi
        '''
        

        '''
        # m2 - max - o(3n), sc - o(2n)
        #  2 1 5 6 2 3
         
        # nse filled with n 
        # pse with -1

        # i*(nse - pse -1)
        # h*w
        n = len(heights)
        st1 =[]
        nse=[n for i in range(n)]  #------imp store n 
        for i in range(n):
            while st1 and heights[st1[-1]] > heights[i]:
                nse[st1.pop()] = i  #------imp store indexex  not next smalles number , we want index of nse

            st1.append(i)

        st2 =[]
        pse=[-1 for i in range(n)] #------imp store -1 
        for i in range(n-1,-1,-1):
            while st2 and heights[st2[-1]] > heights[i]:
                pse[st2.pop()] = i   #------imp store indexex

            st2.append(i)
        # print(nse)
        # print(pse)
        # heights = [2,1,5,6,2,3]
        # nse            2
        # pse            1
        maxi = 0
        for i in range(n):
            area = heights[i] * ( nse[i] - pse[i] - 1)   #--imp len is nse-pse-1 -- dont forget -1
            maxi = max(area,maxi)
        return maxi
        '''
        


        

        

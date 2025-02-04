https://leetcode.com/problems/maximal-rectangle/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 2.then apply largest hist areea reactangle - https://leetcode.com/problems/largest-rectangle-in-histogram/
        # pass each row as a 1d array
        def largest_hist_reactangle(heights):
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
            while st:
                top = st.pop()
                nse = n
                if st:
                    pse = st[-1]
                else:
                    pse = -1
                maxi = max(maxi,heights[top] * (nse-pse-1) )
            return maxi

        # 1.use prefix sum to calucalte height of a histogram bar - o(mn)
        # imp- if its atsrt from 0 - u dont add
        n = len(matrix) #rowx
        m = len(matrix[0]) #cols
        psum = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m): # col1
            sumj = 0
            for i in range(n): # go to all rows
                sumj = sumj + int(matrix[i][j])   #--- matrix has string so convert into int
                if matrix[i][j] == '0':   #- string not int 0
                    sumj = 0  #--vimp if base is 0 - no topsum
                psum[i][j] = sumj
        maxi = 0
        # traverse for each row o(n) traveral* o(2n)for hist
        for i in range(n):
            maxi = max(maxi,largest_hist_reactangle(psum[i]))
        return maxi

https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, h: List[int]) -> int:


        maxi = 0
        n = len(h)
        i =0
        j =n-1


        while i <j:
            maxi = max(maxi,min(h[i],h[j]) * (j-i))
            
            if h[i]<h[j]:
                i+=1
            else:
                j-=1

        return maxi




        '''
        
        area=0
        i = 0
        n = len(height)
        j = n-1
        maxi =0
        while i <j:
            area = min(height[i],height[j]) * (j-i)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            maxi = max(maxi,area)

        return maxi

        '''

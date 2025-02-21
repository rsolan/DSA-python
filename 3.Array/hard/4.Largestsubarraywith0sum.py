https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1?category%5B%5D=Hash&company%5B%5D=Amazon&page=1&query=category%5B%5DHashcompany%5B%5DAmazonpage1company%5B%5DAmazoncategory%5B%5DHash&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-subarray-with-0-sum


class Solution:
    def maxLen(self, arr):
        # code here
        #  [15, -2, 2, -8, 1, 7, -15, 23]
        #0  15   13  15  7  8 15  0
        
        d={}
        d[0]=-1
        maxi = 0
        n = len(arr)
        s=0
        for i in range(n):
            s+=arr[i]
            if s-0 in d:
                maxi = max(maxi, i-d[s])
                
            if s in d:continue #- store first occ for largest
            else:
                d[s] = i
                
        return maxi

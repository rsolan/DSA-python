https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=leaders-in-an-array

class Solution:
    def leaders(self, arr):
        # code here
        # leaders - who have everything smaller after them
        # note - last el is always leader
        '''
        # m1 - bruteforce- n2 - TLE
        n = len(arr)
        ans=[]
        for i in range(n):
            lead = True
            for j in range(i+1,n):
                if arr[i] < arr[j]:
                    lead = False
                    break
                
            if lead:
                ans.append(arr[i])
                
        return ans
        '''
        
        # M2 - go from backward  n-1 to 1 -> o(n) +nlogn to reverse
        # if curr el is greater than maxi to its left , than its leader
        #  [16, 17, 4, 3, 5, 2]
        #  17 is greater than maxi to its left that is 5 , so 17 is leader
        # edge case - = sign
        
        maxi = -float('inf')
        n = len(arr)
        ans = []
        for i in range(n-1,-1,-1):
            if arr[i]>=maxi:    #61 61 17  -> 61 61 17 is ans and not 61 17 --> so = is reqd
                ans.append(arr[i])
                maxi = arr[i]
                
        return reversed(ans)  #not use ans.reverse()xxxxxx
                

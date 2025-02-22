https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1


class Solution:
    def maximumSumSubarray (self,arr,k):
        
        
        n = len(arr)
        s =0
        for i in range(k):
        	s=s+arr[i]
        
        maxi = s
        inc = k
        exl=0
        
        while inc<n:
        	s=s+arr[inc]
        	s=s-arr[exl]
        
        	maxi = max(maxi,s)
        	inc+=1
        	exl+=1
        
        return maxi
        
        '''
        # code here 
        
        # m1 - O(N) - FIXED SLIDING WINDOW
        
        # # STEP1 - PREPROCESS FOR FIRST K WINDOW SIZE
        # n = len(arr)
        # sumj=0
        # for i in range(k):
        #     sumj= sumj+arr[i]
        # # STEP2 - MOVE WIN TILL K REACHES N
        # inc= k
        # exl =0
        # maxi = sumj
        # while inc!=n:
        #     sumj = sumj+ arr[inc] - arr[exl]
        #     maxi = max(maxi,sumj)
        #     inc+=1
        #     exl+=1
        # return maxi
        
        
        # M2 - BRUTEFORCE O(N*K) - TLE
        n = len(arr)
        maxi = -float('inf')
        for i in range(n-k+1):  # so 0 to n-k - included n-k
            sumj=0
            for j in range(i,i+k):
                sumj = sumj + arr[j]
            maxi = max(maxi,sumj)
            
        return maxi
                
            
        # OR  
        # i from n-k+1
        # j from k
        # ind =  i+j

        
        
        
        
        # maxi = - float('inf')
        # n = len(arr)
        # for i in range(n):
        #     sumj = 0
        #     rn = k
        #     j = i
            
        #     while rn!=0 and j<n:
        #         rn-=1
        #         sumj= sumj+arr[j]
        #         j+=1
                
        #     if j==n:
        #         sumj = 0
        #     maxi = max(maxi,sumj)
            
        # return maxi
        
        # arr[] = [100, 200, 300, 400]
                           
        #                   j
        #               1         0        
        #              200 + 300
        
        '''
                

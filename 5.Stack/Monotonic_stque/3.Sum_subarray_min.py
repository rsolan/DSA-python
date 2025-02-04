# https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''      
        # m1 - tle -f ind all subarrays and take mini and keep on adding -O(N2)
        tot = 0
        for i in range(n):
            mini  =arr[i]
            for j in range(i,n):
                mini = min(mini,arr[j])
                tot = (tot+ mini) %MOD

        return tot
        '''



        # m2 - nse and pse - O(2N+2N+N)
        # nse - initialize by n
        # pse use prev smaller and equal el - - 1
        # i -> (i-pse) * (nse-i) * i

        n = len(arr)
        pse =[-1 for _ in range(n)]
        st = []
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:  #- prev smaller and equal
                st.pop()
            if st:
                pse[i] = st[-1] #- storing index
            else:
                pse[i] = -1  
            st.append(i)

            
        nse =[n for _ in range(n)]
        st =[]
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st:
                nse[i] = st[-1] #- storing index
            else:
                nse[i] = n  
            st.append(i) #-- storing indexes

        sumj = 0
        MOD = 10**9 + 7  # Required to avoid overflow
        for i in range(n):
            sumj = (sumj + ((i-pse[i])* (nse[i]-i) *arr[i])%MOD)%MOD    #- MOD AT EAH STEP
            # 3NUMS[I] ha contribution in i-pse and nse-i range, so mult by nums[i] also 

        return sumj
        

# https://leetcode.com/problems/sum-of-subarray-ranges/description/

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        '''
        # m1 - find all subarrays and take DIFF and keep on adding -O(N2)
        n = len(nums)
        tot = 0
        for i in range(n):
            mini  =nums[i]
            maxi = nums[i]
            for j in range(i,n): #optimization - same el will give total = 0 as max-min = 0,so start with i+1
                mini = min(mini,nums[j])
                maxi = max(maxi,nums[j])
                tot = tot + (maxi-mini) 

        return tot
'''
        # m2 -
        # sum of subarray maximum - sum of subarray mini
        # https://leetcode.com/problems/sum-of-subarray-minimums/

        # STEP 1 - CALCULATE SUM OF SUBARRAY MINIMUM
        n = len(nums)
        pse =[-1 for _ in range(n)]
        st = []
        for i in range(n):
            while st and nums[st[-1]] > nums[i]:  #- prev smaller and equal
                st.pop()
            if st:
                pse[i] = st[-1] #- storing index
            else:
                pse[i] = -1  
            st.append(i)

            
        nse =[n for _ in range(n)]
        st =[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st:
                nse[i] = st[-1] #- storing index
            else:
                nse[i] = n  
            st.append(i) #-- storing indexes

        sum_mini = 0
       
        for i in range(n):
            sum_mini = (sum_mini + ((i-pse[i])* (nse[i]-i) *nums[i]))    #- MOD AT EAH STEP
            # 3NUMS[I] ha contribution in i-pse and nse-i range, so mult by nums[i] also 

        

        # STEP 2 - CALCULATE SUM OF SUBARRAY MAXIMUM
        # i will be mx wil lnge and pge  -> (i-pge)(nge-i)* nums[i]

        pge =[-1 for _ in range(n)]
        st = []
        for i in range(n):
            while st and nums[st[-1]] < nums[i]:  #- prev smaller and equal
                st.pop()
            if st:
                pge[i] = st[-1] #- storing index
            else:
                pge[i] = -1  
            st.append(i)

            
        nge =[n for _ in range(n)]  #- imp store n
        st =[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            if st:
                nge[i] = st[-1] #- storing index
            else:
                nge[i] = n  
            st.append(i) #-- storing indexes

        sum_maxi = 0
        for i in range(n):
            sum_maxi = (sum_maxi + ((i-pge[i])* (nge[i]-i) *nums[i]))   #- MOD AT EAH STEP
            # 3NUMS[I] ha contribution in i-pse and nse-i range, so mult by nums[i] also 


        return sum_maxi - sum_mini

        

https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # nums = [1,2,3], k = 3
        # [1,2]
        # [3]
        # sorting can help -> more than k - break 
        # -1000 <= nums[i] <= 1000
        # -6 1 2 2 2 3 6  -> 2 pointer xx
        
        # [2,2,2,3,1,6,-6]  k = 6

        # 2 subarraye tahts usms to 6 ending at 8

        # d[sum] = freq

        # tc - o(n)  and using dict
        # sc - o(n) for d

        # [2,2,2,-4,1,3,2,-6,6] - arr
        # [2,4,6, 2,3,6,8,2, 8] - psum - use dict
        # freq dynamically solve --> not precalculated

        d = defaultdict(int)
        d[0] = 1  # for case when sum==k
        summ =0
        cnt =0
        for i in nums:
            summ+=i   #8
            if summ-k in d: #8-6 = 2
                cnt = cnt + d[summ-k]   #freq of 2 is 2 till now so cnt should be inc by 2

            d[summ]+=1 #inc the freq   # inc the d[8] by 1


        return cnt

        



        ''' - not working
        count = 0
        psum =0
        n = len(nums)
        d={}
        for i in range(0,n):
            psum = psum + nums[i]

            
            if psum == k:
                count+=1

            rem = psum - k
            if rem in d:
                count+=1
            if psum not in d:       
                d[psum] = i  #dont update if the psum already exist
        return count
        '''

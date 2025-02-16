All possible patters from Subsequence

1. Print All the Subsequence
2. Print all Sq which sums to K
3. Print only 1st Sq which sums to K
4. Print the count of Sq which sums to K
tc - 2^n - 2 option for each index t/nt


1) COUNT FOR HOW MANY SUM == K
'''
        # use - this str fo count
        if true - retunr 1
        else - return 0
        l()
        r()
        return l+r
        
        
        if n rec calls - n queen
        if true - retunr 1
        else - return 0
        s = 0
        for i in n:
            s+=f()
        return s
        '''
        

#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
	    
		# code here
		def rec(ind,arr,s):
		    n = len(arr)
	            if s> sum : return 0
		    if ind == n:
		        if s == target:
		            return 1
	            return 0
		            
		    s = s+arr[ind]
		    left = rec(ind+1,arr,s)
		    
		    s = s-arr[ind]
		    right = rec(ind+1,arr,s)
			
		    return left+right
		    
        s=0
        return rec(0,arr,s)
         
        
		''' - DONT UES THIS
		def rec(ind,arr,ans,s,cnt):
		    n = len(arr)
		    if ind == n:
		        if s == target:
		            cnt[0]+=1
	            return
		            
		    ans.append(arr[ind])
		    s = s+arr[ind]
		    rec(ind+1,arr,ans,s,cnt)
		    
		    s = s-arr[ind]
		    ans.pop()
		    rec(ind+1,arr,ans,s,cnt)
		    
        cnt =[0]
        ans = []
        s=0
        rec(0,arr,ans,s,cnt)
        return cnt[0]
        '''
        #




2) RETURN TRUE OR FALSE IF ANY WITH SUM = K
https://www.naukri.com/code360/problems/subset-sum_630213?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

from typing import *

def isSubsetPresent(n:int, k: int, arr: List[int]) -> bool:
    # Write your code here.
    def rec(ind,arr,ans,s):
        n = len(arr)
        if ind == n:
            if s == k:
                return True
            return False
                
        ans.append(arr[ind])
        s = s+arr[ind]
        if rec(ind+1,arr,ans,s):
            return True
        rec(ind+1,arr,ans,s)
        
        s = s-arr[ind]
        ans.pop()
        if rec(ind+1,arr,ans,s):
            return True
        # rec(ind+1,arr,ans,s)

        return False
		    
    
    ans = []
    s=0
    if rec(0,arr,ans,s):
        return True
    return False


3) print patterns whose sum = k
class Solution:
    def print(self, arr: List[int], target: int) -> List[List[int]]:
        
        def rec(ind,arr,ans,s,out):
            n = len(arr)
            # if ind == n:
            if s == target:
                out.append(ans[:])
                return

            # if s > target or ind>=n:
            #     return
                    
            ans.append(arr[ind])
            s = s+arr[ind]
            rec(ind+1,arr,ans,s,out)
            
            s = s-arr[ind]
            ans.pop()
            rec(ind+1,arr,ans,s,out)

            return out
                
        out = []
        ans = []
        s=0
        return rec(0,arr,ans,s,out)


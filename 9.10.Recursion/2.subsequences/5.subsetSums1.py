https://www.geeksforgeeks.org/problems/subset-sums2234/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=subset-sums


#User function Template for python3
class Solution:
	def subsetSums(self, arr):
		# code here
		'''
		sum of all subsets - sum of subset1, sum of subset2
        [],2,3,23
        for n no-> 2^subset
        so we have out = [2^n el - each el is sum of that subset]
        
        '''
        def rec(ind,arr,s,ans):
            n  =len(arr)
            if ind ==n:
                ans.append(s)
                return #--- vvv imp to return in base case
                
            # ds.append(arr[ind]) ->no need as we just need sum
            rec(ind+1,arr,s+arr[ind],ans)
            
            rec(ind+1,arr,s,ans)
            
            
        s = 0
        ans =[]
        rec(0,arr,s,ans)
        return ans

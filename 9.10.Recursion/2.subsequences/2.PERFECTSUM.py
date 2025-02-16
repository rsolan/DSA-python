Notes to Self :-
All possible patters from Subsequence

1. Print All the Subsequence
2. Print all Sq which sums to K
3. Print only 1st Sq which sums to K
4. Print the count of Sq which sums to K


*Note In order to understand Printing all subsequence in absolute clear way..... Just take the example which striver gave in previous video

Now create a table of all the output and match it with the power set. A magic will happen and you will be totally blown away


https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=perfect-sum-problem
TLE
#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
		# code here
		def rec(ind,arr,ans,s,cnt):
		    n = len(arr)
		    if ind == n:
		        if s == target:
		            cnt+=1
	            return
		            
		    ans.append(arr[ind])
		    s = s+arr[ind]
		    rec(ind+1,arr,ans,s,cnt)
		    
		    s = s-arr[ind]
		    ans.pop()
		    rec(ind+1,arr,ans,s,cnt)
		    
        cnt =0
        ans = []
        s=0
        rec(0,arr,ans,s,cnt)
        return cnt

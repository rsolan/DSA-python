# subsequence - contigous/non-contigous seq which follows the order
3 el - 2^3 = 8 subseq
[312]  -> [] , 312 , 3 , 1 ,2 , 31,12, 32   ---->power set
# sub array - need to be contigous (and follows order



tc - 2^n - 2 option for each index t/nt

https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def recursive_fun(ind,ans,nums,out):
            if ind==n:
                # print(ans)
                out.append(ans[:]) #----------vvimp # Append a copy of ans and not ans
                return
                # can add edgec ase - 
                # if n==0:
                #     out.append("[]")


            # ans.append(nums[ind])
            # recursive_fun(ind+1,ans,nums,out)
            # ans.pop()
            # recursive_fun(ind+1,ans,nums,out)
            recursive_fun(ind+1,ans,nums,out)
            ans.append(nums[ind])
            recursive_fun(ind+1,ans,nums,out)
            ans.pop()


        out = []
        ans = []
        recursive_fun(0,ans,nums,out)

        return out

'''
u can push later also - so no need to pop -> rec call , add, rec call, pop


Since ans is a mutable list, when you append it directly to out, subsequent modifications to ans also affect the previously stored lists in out. To fix this, you should append a copy of ans instead of appending it directly.
--
To create subsets, point is that we have two choices for each number.

⭐️ Points

Include current number
Not include current number'''

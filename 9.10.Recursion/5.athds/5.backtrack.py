https://leetcode.com/problems/subsets/  
integer array nums of unique elements, return all possible subsets(the power set).
        
# bt method

        ds=[]
        ans =[]
        n = len(nums)
        def rec(i,ds):
            ans.append(ds[:])
            for j in range(i,n):
                ds.append(nums[j])
                rec(j+1,ds)
                ds.pop()	

        # nums.sort() - no need
        rec(0,ds)
        return ans



https://leetcode.com/problems/subsets-ii/
Given an integer array nums that may contain duplicates, return all possible subsets(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
# bt , dup - sort and j cond
        out = []
        ds = []
        n = len(nums)

        def rec(i,ds):
            
            out.append(ds[:])
                
            for j in range(i,n):
                if j!=i and nums[j]==nums[j-1]: continue
                ds.append(nums[j])
                rec(j+1,ds) # j can move
                ds.pop()

        nums.sort()
        rec(0,ds)
        return out



https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

# distinct - NO DUPS - SO NO SORT NEEDED
        # bt 
        out =[]
        ds =[]
        n = len(arr)
        def rec(i,s,ds):
            if s == t:
                out.append(ds[:])
                return

            if s>t:
                return

            for j in range(i,n):
                ds.append(arr[j])
                rec(j,s+arr[j],ds)  #---same index
                ds.pop()

            
        rec(0,0,ds)
        return out



https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

        # duplicates - need to be sorted , and j,j-1 cond
        # bt
        arr.sort()
        def rec(ds,ind,out,summ):
            if summ == target:
                out.append(ds[:])
                return

            # if ind == n:
            #     return

            if summ > target:
                return

            # lis1 = ds[:]
            # lis2=ds[:]
            for j in range(ind,n):
                if j> ind and arr[j] == arr[j-1]:  #-- remove duplicates , 
                # 125 and 125 - only 1 inlc , but we have to take 112
                # so 1s can be taken for diff indexes 
                    continue
                ds.append(arr[j])
                rec(ds,j+1,out,summ+arr[j])
                ds.pop()
        out = [] #-- no need of set
        ds= []
        summ = 0
        n = len(arr)
        
        rec(ds,0,out,summ)
        return out

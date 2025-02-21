https://leetcode.com/problems/subsets/  
integer array nums of unique elements, return all possible subsets(the power set).
        
ds=[]
ans =[]
n = len(nums)
def rec(i,ds):
    if i == n:
        ans.append(ds[:])
        return

    ls1 = ds[:]
    ls2=ds[:]

    ls1.append(nums[i])
    rec(i+1,ls1)	
    rec(i+1,ls2)
    

# nums.sort() -- no need
rec(0,ds)
return ans



https://leetcode.com/problems/subsets-ii/
Given an integer array nums that may contain duplicates, return all possible subsets(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
# recrusion , use of out set and tuple ;  make a copy dup - sort and out as set
        out = set()
        ds = []
        n = len(nums)

        def rec(i,ds):
            if i == n:
                out.add(tuple(ds[:]))  #-- use of set and then tupple add
                return

            ls1 = ds[:]
            ls2 = ds[:]

            ls1.append(nums[i])
            rec(i+1,ls1)

            rec(i+1,ls2)

        nums.sort()  #-- imp to sort
        rec(0,ds)
        return list(out)



https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

# distinct - NO DUPS - SO NO SORT NEEDED
        # recursion
        out =[]
        ds =[]
        n = len(arr)
        def rec(i,s,ds):
            if i == n and s == t:
                out.append(ds[:])
                return
            if i ==n:
                return

            if s>t:
                return
            ls1 = ds[:]
            ls2=ds[:]
            ls1.append(arr[i])
            # ds.append(arr[i]) #- or make 2 copys
            rec(i,s+arr[i],ls1)  #--- imp to go with i and not i+1
            # ds.pop()
            rec(i+1,s,ls2)
            
        rec(0,0,ds)
        return out



https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

        ds=[]
        out =set()
        n = len(arr)
        def rec(i,ds,s):
            if i==n and s==t:
                out.add(tuple(ds[:]))
                return
            if i==n:
                return
            if s>t:
                return
            
            ls1 = ds[:]
            ls2 = ds[:]
            
            ls1.append(arr[i])	
            rec(i+1,ls1,s+arr[i])

          # Include arr[i]
        # ds.append(arr[i])
        # rec(i + 1, s + arr[i])
        # ds.pop()  # Backtrack

            #  Skip duplicates ---> missingcondition
            while i + 1 < n and arr[i] == arr[i + 1]:
                i += 1

            rec(i+1,ls2,s)

        arr.sort()
        rec(0,ds,0)
        return list(out)



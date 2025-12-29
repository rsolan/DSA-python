# 1 subsets question


https://leetcode.com/problems/subsets/  
integer array nums of unique elements, return all possible subsets(the power set).



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ds =[]
        ans =[]
        n = len(nums)


        def rec(i,ds):
            if i == n:
                ans.append(ds[:])  # pass copy ds[:]. and not refernce of ds ie ds
                # 1why ans.append(ds)  is wrong
                return  #2 why 'return ans' is wrong you cant return ans for each end call , so just here do simple 'return'


            # copy
            ls1= ds[:] # include
            ls2 = ds[:]  # exclude

            
            ls1.append(nums[i]) # 3 MODIFY COPY LS1 and not reference ds
            rec(i+1,ls1)
            rec(i+1,ls2)

        rec(0,ds)
        return ans

        # 4 return rec(0,ds) - u r not returning inside rec func - so store in ans one by one and then in end return ans

'''
#  imp - 
ds keeps on changing recursion 
so ds can change when kept inside ans also
so we store copy of ds in ans
ans.append(ds[:])  # pass copy ds[:]. and not refernce of ds ie ds
'''





===
EXPLAIN PETAH lol

                            []
                 ┌───────────┴───────────┐
               [10]                       []
          ┌──────┴──────┐          ┌──────┴──────┐
     [10,20]           [10]       [20]            []
   ┌────┴────┐     ┌────┴────┐ ┌────┴────┐  ┌────┴────┐
[10,20,30][10,20] [10,30] [10] [20,30] [20] [30]     []

--

                         rec(i=0, ds=[])

                 ┌───────────────┴───────────────┐
        rec(i=1, ds=[10])                    rec(i=1, ds=[])

          ┌──────────────┴──────────────┐      ┌──────────────┴──────────────┐
 rec(i=2,[10,20])     rec(i=2,[10])   rec(i=2,[20])        rec(i=2,[])


rec(i=0, ds=[])
ls1=[10], ls2=[]
│
├── rec(i=1, ds=[10])
│   ls1=[10,20], ls2=[10]
│   │
│   ├── rec(i=2, ds=[10,20])
│   │   ls1=[10,20,30], ls2=[10,20]
│   │   ├── rec(3,[10,20,30])
│   │   └── rec(3,[10,20])
│   │
│   └── rec(i=2, ds=[10])
│       ls1=[10,30], ls2=[10]
│       ├── rec(3,[10,30])
│       └── rec(3,[10])
│
└── rec(i=1, ds=[])
    ls1=[20], ls2=[]
    │
    ├── rec(i=2, ds=[20])
    │   ls1=[20,30], ls2=[20]
    │   ├── rec(3,[20,30])
    │   └── rec(3,[20])
    │
    └── rec(i=2, ds=[])
        ls1=[30], ls2=[]
        ├── rec(3,[30])
        └── rec(3,[])

           Key Understanding

i → depth / index in nums

ds → current subset

ls1 → include nums[i]

ls2 → exclude nums[i]

Leaves (i == n) → valid subsets

This is exactly how power set = 2ⁿ is formed.


=======









                   

# 2 subset2 

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ds =[]
        ans = set() # 1 use sets so ans doesnt have duplicates
        n = len(nums)

        def rec(i,ds):
            if i ==n:
                ans.add(tuple(ds[:]))
                # add for sets and not append - wrong ans.append(ds[:]) 
                #  2 u cannt add list to ans set - wrong ans.add(ds[:])  - TypeError: unhashable type: 'list'
                return
            
            ls1=ds[:]
            ls2 = ds[:]

            ls1.append(nums[i])
            rec(i+1,ls1)
            rec(i+1,ls2)

        # 3 - vvvimp -- sort nums
        nums.sort()
        rec(0,ds)
        return list(ans)   #---------------vvvimppp always check what to return - U DONT RETURN SET AS QUESTION SAYS RETURN LIST



'''

✅ Why set works

A set:

Stores unique elements only

Automatically removes duplicates

out = set()
out.add(...)


If the same subset appears again → it is ignored

✔ This solves the duplicate-subset problem.


==

Why do we sort nums?
Without sorting
nums = [2, 1, 2]


Possible subsets:

[2,1]  and  [1,2]


These are logically the same subset, but Python thinks they are different.

After sorting
nums = [1, 2, 2]


Now:

[1,2] and [1,2]  → identical


✔ Sorting ensures same elements appear in same order, so duplicates match.


===



3️⃣ Why do we add a tuple to the set?
🚫 Why NOT ds[:] directly?
out.add(ds[:])  ❌ ERROR


Python error:

TypeError: unhashable type: 'list'

🔑 Key Rule in Python

set can only store hashable (immutable) types.  ---- set dont have index

list is mutable → unhashable

tuple is immutable → hashable

✅ Correct way
out.add(tuple(ds[:]))


You are converting:

[1, 2] → (1, 2)


Now Python can:

Hash it

Compare it

Store it uniquely

4️⃣ Why do we still use ds[:] before tuple?
Reason

ds changes during recursion.

If you do:

out.add(tuple(ds))


This usually works, but best practice is:

out.add(tuple(ds[:]))


Because:

ds[:] → snapshot of current subset

No accidental mutation issues

Clear intent

5️⃣ Putting it all together
if i == n:
    out.add(tuple(ds[:]))


✔ ds[:] → make a copy
✔ tuple(...) → make it immutable
✔ out.add(...) → store unique subsets




Final Summary
Concept	Why
set	removes duplicate subsets
sort()	ensures same order for duplicates
tuple()	lists are unhashable
ds[:]	safe snapshot of current subset
'''

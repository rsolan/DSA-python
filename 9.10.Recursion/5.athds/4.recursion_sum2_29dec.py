
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ds=[]
        out=[]
        n = len(candidates)
        def rec(i,s,ds):
            if i==n and s==target:
                out.append(ds[:])
                return
            
            if i==n:
                return
            if s>target:
                return

            ls1=ds[:]
            ls2=ds[:]
            ls1.append(candidates[i])

            rec(i,s+candidates[i],ls1).  # i as i can be taken more than once
            rec(i+1,s,ls2)

        #no duplicates so no sort
        rec(0,0,ds)
        return out
      
  

Yes 👍 — let’s draw the Combination Sum recursion tree in the same visual level-by-level style you asked for.

Example

arr = [2,3,5], target = 8
rec(i, s, ds)

🌳 LEVEL-WISE TREE (STRUCTURED VIEW)
🔹 LEVEL 0
rec(i=0, s=0, ds=[])

                    rec(i=0, s=0, ds=[])

🔹 LEVEL 1

(from index 0, value = 2)

ls1 = [2]     (take 2 → same i)
ls2 = []      (skip 2 → i+1)

           ┌───────────────┴───────────────┐
  rec(i=0, s=2, ds=[2])           rec(i=1, s=0, ds=[])

🔹 LEVEL 2

From rec(i=0, s=2, ds=[2])
From rec(i=1, s=0, ds=[])

rec(i=0, s=2, ds=[2]) →
   ls1 = [2,2]
   ls2 = [2]

rec(i=1, s=0, ds=[]) →
   ls1 = [3]
   ls2 = []

      ┌──────────────┴──────────────┐     ┌──────────────┴──────────────┐
rec(i=0,s=4,[2,2])  rec(i=1,s=2,[2])  rec(i=1,s=3,[3])   rec(i=2,s=0,[])

🔹 LEVEL 3
rec(i=0,s=4,[2,2]) →
   ls1=[2,2,2]
   ls2=[2,2]

rec(i=1,s=2,[2]) →
   ls1=[2,3]
   ls2=[2]

rec(i=1,s=3,[3]) →
   ls1=[3,3]
   ls2=[3]

rec(i=2,s=0,[]) →
   ls1=[5]
   ls2=[]

 ┌──────────┴──────────┐ ┌──────────┴──────────┐ ┌──────────┴──────────┐ ┌──────────┴──────────┐
rec(0,6,[2,2,2]) rec(1,4,[2,2]) rec(1,5,[2,3]) rec(2,2,[2]) rec(1,6,[3,3]) rec(2,3,[3]) rec(2,5,[5]) rec(3,0,[])

🔹 LEVEL 4 (IMPORTANT SUCCESSES)
rec(0,6,[2,2,2]) →
   ls1=[2,2,2,2]  ✅ sum=8
   ls2=[2,2,2]

rec(1,5,[2,3]) →
   ls1=[2,3,3]    ✅ sum=8
   ls2=[2,3]

rec(2,3,[3]) →
   ls1=[3,5]      ✅ sum=8

 ┌──────────┴──────────┐     ┌──────────┴──────────┐      ┌──────────┴──────────┐
[2,2,2,2]        stop        [2,3,3]        stop         [3,5]          stop

✅ FINAL OUTPUT
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

🧠 HOW TO READ THIS TREE

Left child → take element (same i)

Right child → skip element (i+1)

Horizontal lines → same recursion level

Vertical depth → deeper recursion

Pruned branches → s > target or i == n

🔑 WHY THIS FORMAT IS IMPORTANT

This exact shape explains:

Why combinations don’t repeat

Why order doesn’t matter

Why reuse works (rec(i, ...))

Why pruning saves time

                   =====

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ds=[]
        out=set() # fails for [2,2,2] if not set why ??
        n = len(candidates)
        def rec(i,s,ds):
            if i==n and s==target:
                out.add(tuple(ds[:]))
                return
            
            if i==n:
                return
            if s>target:
                return

            ls1=ds[:]
            ls2=ds[:]
            ls1.append(candidates[i])

            rec(i+1,s+candidates[i],ls1)

            while i+1<n and candidates[i]==candidates[i+1]:  # not if - as can be more adjacentdupl
                i=i+1

            rec(i+1,s,ls2)

        candidates.sort() # as cand can have duplicates

        rec(0,0,ds)
        return list(out)


        # [1,2,2,3]

        # [1,2] and [1,2] same result - so we need to skip duplicates


'''

🔑 What’s DIFFERENT in Combination Sum II?

Compared to Combination Sum I:

Rule	Combination Sum I	Combination Sum II
Can reuse same element	✅ Yes	❌ No
Input may have duplicates	❌ No	✅ Yes
Result must be unique	✅	✅

So here we must handle two things at once:

Each index can be used only once

Duplicate values in input must NOT create duplicate combinations

🔴 The CORE PROBLEM (why duplicates happen)

Example:

arr = [1,1,2], target = 3


Sorted:

[1,1,2]


Possible recursion paths:

take arr[0]=1 → take arr[2]=2 → [1,2]
take arr[1]=1 → take arr[2]=2 → [1,2]


❌ SAME combination [1,2] generated twice
But from different indices (arr[0] vs arr[1])

🔑 Why sorting is REQUIRED
arr.sort()


Sorting ensures:

duplicates are adjacent


This makes it possible to skip duplicates safely.

⭐ The EXTRA CONDITION (THE KEY LINE)
while i + 1 < n and arr[i] == arr[i + 1]:
    i += 1

🔥 What this does

When you SKIP an element, you also skip all of its duplicates at the same recursion level.

🧠 Why skip ONLY in the "exclude" path?

Your structure:

# include
ls1.append(arr[i])
rec(i+1, ls1, s+arr[i])

# skip duplicates
while i + 1 < n and arr[i] == arr[i + 1]:
    i += 1

# exclude
rec(i+1, ls2, s)

Intuition:

If you include arr[i], you want to allow future paths

If you exclude arr[i], then excluding its duplicates too prevents duplicate combinations

🔍 Example Dry Intuition
Input
arr = [1,1,2], target = 3

At i=0
Include 1 → path starts with [1]
Exclude 1 → should NOT start another [1] from index 1


So when excluding:

skip arr[1] also
jump directly to arr[2]


This prevents:

[1,2] coming twice

🔴 What happens WITHOUT the skip condition?

Without:

while i+1 < n and arr[i] == arr[i+1]:


You get:

[1,2] from arr[0]
[1,2] from arr[1]


Even if you use a set, recursion still does extra work ❌

🟢 Why your set + tuple STILL works

You are doing:

out.add(tuple(ds[:]))


This:

removes duplicates at the end
               '''

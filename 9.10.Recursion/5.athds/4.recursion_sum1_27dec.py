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



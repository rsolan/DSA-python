# subsets question


https://leetcode.com/problems/subsets/  
integer array nums of unique elements, return all possible subsets(the power set).
        



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



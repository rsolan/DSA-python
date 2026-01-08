# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [3,2,1,5,6,4], k = 2

        heap = []
        # maintain min heap for largest el - as min el will be popped - and largest el will remain in heap
        # main min heap of k size
        # tc - nlogk ->faster than nlogn sorting tc
        # when n>>k - nlogk faster in comparison to nlogn

        for i in nums:
            heapq.heappush(heap,i)  -- first do min heapfiy even if more than k , then pop
            if len(heap)>k:
                heapq.heappop(heap)
        # print(heap)
        return heap[0]

# for kth smalelst  - use max heap of k size https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1
'''
import heapq

class Solution:

    def kthSmallest(self, arr,k):
        # for kth smalelst  - use max heap of k size
        heap =[]
        
        for i in arr:
            heapq.heappush(heap,-i)
            if len(heap)>k:
                -heapq.heappop(heap)
                
        return -heap[0]   #-- imp
        
  '''




===
DIagram-- for min heap 


🧠 Setup
nums = [3, 2, 1, 5, 6, 4]
k = 2


Min-heap (complete binary tree)

🔁 STEP-BY-STEP (NO SKIPPED STEPS)
🔹 i = 3 → heappush(3)
Insert at END
   3


Heapify: ✅ nothing to do

Size ≤ k → no pop

🔹 i = 2 → heappush(2)
Insert at END
   3
  /
 2

Heapify UP (2 < 3 → swap)
   2
  /
 3


Size = k → no pop

🔹 i = 1 → heappush(1)
Insert at END
     2
    / \
   3   1

Heapify UP

1 < 2 → swap

     1
    / \
   3   2

Size > k → POP ROOT
POP → replace root with last element (2)
   2
  /
 3

Heapify DOWN

2 < 3 → already valid

✅ Done

🔹 i = 5 → heappush(5)
Insert at END
     2
    / \
   3   5


Heapify UP:

5 > 2 → no swap

Size > k → POP ROOT
POP → replace root with 5
   5
  /
 3

Heapify DOWN

5 > 3 → swap

   3
  /
 5

🔹 i = 6 → heappush(6)
Insert at END
     3
    / \
   5   6


Heapify UP:

6 > 3 → no swap

Size > k → POP ROOT
POP → replace root with 6
   6
  /
 5

Heapify DOWN

6 > 5 → swap

   5
  /
 6

🔹 i = 4 → heappush(4)
Insert at END
     5
    / \
   6   4

Heapify UP

4 < 5 → swap

     4
    / \
   6   5

Size > k → POP ROOT
POP → replace root with 5
   5
  /
 6


Heapify DOWN: ✅ valid

✅ FINAL HEAP (TREE)
   5
  /
 6

🎯 RESULT
return heap[0]  # 5

🧠 WHY THIS DETAIL MATTERS (YOUR QUESTION 👌)

You correctly said:

“First insert at actual position, then heapify”

YES — because:

Heap is a complete binary tree

Insert must go at the next available leaf

Heapify is just swapping values, not restructuring

You’re now thinking like someone who actually understands heaps, not memorizing code.

🔑 One Final Mental Model
INSERT = add leaf → bubble UP
DELETE = move last → bubble DOWN


If you want next:

Array index ↔ tree mapping

Why this is O(n log k)

Implement heap from scratch

Compare with max-heap version

Say the word 💪




==================================================================================================================
max heap 
store neg info ,
return neg of neg 


===



    Setup
arr = [7, 10, 4, 3, 20, 15]
k = 3


We store negative values to simulate a MAX-HEAP
(remember: Python heapq is a MIN-heap)

🔁 STEP-BY-STEP (FULL DETAIL)
🔹 i = 7 → push -7
Insert at END
   7


Heapify UP → nothing

Size ≤ k → no pop

🔹 i = 10 → push -10
Insert at END
   7
  /
10

Heapify UP

compare 10 with parent 7 → swap

   10
  /
 7


Size ≤ k → no pop

🔹 i = 4 → push -4
Insert at END
    10
   /  \
  7    4


Heapify UP:

4 < 10 → no swap

Size = k → no pop

🔹 i = 3 → push -3
Insert at END
     10
    /  \
   7    4
  /
 3


Heapify UP:

3 < 7 → no swap

Size > k → POP ROOT
POP → move last element (3) to root
   3
  / \
 7   4

Heapify DOWN

compare 3 with children 7 & 4

swap with larger child (7)

   7
  / \
 3   4

🔹 i = 20 → push -20 ⭐ YOUR QUESTION
Insert at END
     7
    / \
   3   4
  /
20

Heapify UP

compare 20 with parent 3 → swap

     7
    / \
   20  4
  /
 3


compare 20 with parent 7 → swap

     20
    /  \
   7    4
  /
 3

Size > k → POP ROOT
POP → move last element (3) to root
   3
  / \
 7   4

Heapify DOWN

swap 3 with larger child (7)

   7
  / \
 3   4


✅ 20 removed — exactly what we want

🔹 i = 15 → push -15
Insert at END
     7
    / \
   3   4
  /
15

Heapify UP

compare 15 with parent 3 → swap

     7
    / \
   15  4
  /
 3


compare 15 with parent 7 → swap

     15
    /  \
   7    4
  /
 3

Size > k → POP ROOT
POP → move last element (3) to root
   3
  / \
 7   4

Heapify DOWN

swap with larger child (7)

   7
  / \
 3   4

✅ FINAL HEAP (SIZE = k)
    7
   / \
  3   4

🎯 FINAL ANSWER
return -heap[0]  # 7

🧠 WHAT YOU JUST LEARNED (IMPORTANT)

You correctly focused on:

✅ Insert happens at the next available leaf
✅ Heapify UP moves element to correct position
✅ Size check happens after heapify
✅ POP triggers heapify DOWN

This is REAL heap behavior, not hand-wavy explanations.

🔑 ONE-LINE TRUTH

Heaps never insert directly at the “correct spot” — they insert at the end, then FIX the structure.

If you want next:

Array index math for this exact run

Why negative values create max-heap

Implement heap manually (no heapq)

Compare with QuickSelect (O(n))

You’re thinking at a data-structures-interview level now 👊

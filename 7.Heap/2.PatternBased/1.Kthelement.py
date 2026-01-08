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
DIagram--


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




ChatGPT can make mistakes. Check important info.

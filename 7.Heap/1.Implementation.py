'''
heap is complete binary tree (bt with 01,2 children filled top to bottom and left to right)

Note - perfect bianry tree has - exact 2 children


OPeration
  1.insertion - logn
  isnert a node in TOP TO BOTTM AND LEFT TO WRIGHT MANNER
  HEAPIFY IT FROM BOTTOM TO TOP (UPWARD HEAPIFY ) -- in the node to root path -> 
  for min heap - keep min in parent ( no relation btw left or right child) - ie  parent < child
  
  
  2.deletion - logn
  delete the root node (min or max) 
  then heapify downward - 
      del root node, last node gets on root , then maintain heapify algo from root to last
  
  
  3. return max or min takes - O(1)
  return root 
  or heap[0]



STORED IN ARRAY 
  heap list [] = 
  for i node 
  parent - i-1//2
  left child - 2i+1
  right child - 2i+2


  diff btw heappsuh and heapify
  visualalgo

  '''



===============

INSERT
INSERT AT END
HEAPIFY MAINTAIN FROM BOTTOM TO TOP 

DELETE
DELETE FROM ROOT
PUSH LAST NODE TO ROOT AND
THEN HEAPIFY FROM TOP TO BOTTOM ( SMALLEST CHILD AT ROOT)




=================
CHATGPT

===
What is a Heap (Quick Reminder)

A heap is:

A complete binary tree

Min-heap rule:
👉 Parent ≤ Children

But in Python, we store it as an array.

Index rules

For index i:

left child  = 2*i + 1
right child = 2*i + 2
parent      = (i - 1) // 2

🔼 INSERT (heappush)
Steps:

Add the new element at the end

Bubble it UP until heap rule is satisfied

🔍 Example: Insert 1 into heap [2, 3, 5]
Step 1: Add at end
[2, 3, 5, 1]


Tree view:

      2
     / \
    3   5
   /
  1

Step 2: Bubble UP (compare with parent)

1 vs parent 3 → swap

[2, 1, 5, 3]


Tree:

      2
     / \
    1   5
   /
  3


1 vs parent 2 → swap

[1, 2, 5, 3]


Tree:

      1
     / \
    2   5
   /
  3


✅ Heap property restored

🔽 DELETE (heappop)

⚠️ In a heap, we always delete the ROOT (min element in min-heap).

🔍 Example: Delete from heap [1, 2, 5, 3]
Step 1: Remove root
remove 1

Step 2: Move last element to root
[3, 2, 5]


Tree:

      3
     / \
    2   5

Step 3: Bubble DOWN

Compare 3 with children 2 and 5

Smallest child = 2  ----------------->> SMALLEST OF BOTH CHILD

Swap

[2, 3, 5]


Tree:

      2
     / \
    3   5


✅ Heap property restored

🧠 Why This is FAST
Height of heap = log n

Insert → bubble UP → O(log n)

Delete → bubble DOWN → O(log n)


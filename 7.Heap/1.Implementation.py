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

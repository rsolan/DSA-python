https://www.geeksforgeeks.org/problems/merge-k-sorted-arrays/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=merge-k-sorted-arrays

import heapq
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, k):
        # code here
        # return merged list
    #             i         j         k     l
    #     {{1,2,3,4},{2,2,3,4},{5,5,6,6},{7,8,9,9}}
        
    #      2 5 7  2 2
    #   5 7 , 3 3
    # ans = 1 2 2
    
    
        heap =[]
        # prepprcess to store 0th index val for al k arrays - val,ind
        for i in range(k):
            heapq.heappush(heap,(arr[i][0],i,0))
    
        # heap =[1257] min heap
        # 1257 - 257
        # 2257 - 257
        # 3257 - 2357 - 357 
        # 3357 - 4357 - 3457 - 457
        # 4457 - 457 - 57 
        # 57 - 67 
        # 7- 67 - 7 - 8 - 9 9 
        
        
        ans =[]
        while heap :
            val,i,j = heapq.heappop(heap) 
            ans.append(val)
            
            if j+1 < k:
                heapq.heappush(heap, (arr[i][j+1],i,j+1))
                    
        return ans

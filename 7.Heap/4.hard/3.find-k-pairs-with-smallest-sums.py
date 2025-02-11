https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # m1 - nm lognmn2logn2

        
        # m2
        # 2k log nm 
        # 2nmlognm
        #          0 1 2
        # nums1 = [1,7,11], 
        # nums2 = [2,4,6], 
        # heap = [  ]
        # 3,0,0 -> 0,1 or 1,0
        # k = 3 2  
        # ans = 0,0
        # vis = 0,0

        n = len(nums1)
        m = len(nums2)
        heap=[]
        heapq.heappush(heap,(nums1[0]+nums2[0],0,0))  #sum,0,0
        vis= set() #--- cant have duplicates
        vis.add((0,0))
        ans =[]

        while heap and k:
            k-=1
            s,i,j = heapq.heappop(heap)
            ans.append((nums1[i],nums2[j]))
            # vis.add((i,j))

            if i<n and j+1<m and (i,j+1) not in vis:
                heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
                vis.add((i,j+1))

            if i+1<n and j<m and (i+1,j) not in vis:
                heapq.heappush(heap,(nums1[i+1]+nums2[j],i+1,j))
                vis.add((i+1,j))

            # print(heap,k,ans,vis)

        return ans






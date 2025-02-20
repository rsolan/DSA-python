https://leetcode.com/problems/rotate-array/


# class Solution:
#     def reverse(self,arr,start,end):
#         i=start
#         j = end-1
#         while i<=j:
#             arr[i],arr[j] = arr[j],arr[i]
#             i+=1
#             j-=1
#         print(arr)

#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        
#         # k = 5 , n = 6
#         # [1, 2, 3, 4, 5, 6]
#         # [1, 6, 5, 4, 3, 2]
#         # [2, 3, 4, 5, 6, 1]
#         n = len(nums)
#         k = k%n
#         self.reverse(nums,0,n-k)
#         self.reverse(nums,n-k,n)
#         self.reverse(nums,0,n)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1.reverse 0 to n-1
        # 2.reverse 0 to k-1
        # 3.reverse k to n-1
        
        # [1, 2, 3, 4, 5, 6, 7]
        # [7, 6, 5, 4, 3, 2, 1]
        # [5, 6, 7, 4, 3, 2, 1]
        # [5, 6, 7, 1, 2, 3, 4]

        n = len(nums)
        k %= n
        print(nums)
        nums.reverse()
        print(nums)
        nums[:k] = reversed(nums[:k])
        print(nums)
        nums[k:] = reversed(nums[k:])
        print(nums)

    '''  
    # left rotate by 1
    temp = nums[0]
    for i in range(n-1):
        nums[i] = nums[i+1]
    nums[n-1]=temp
    '''

    # left rotate by k
        # 3.reverse 0 to n-1
        # 1.reverse 0 to k-1
        # 2.reverse k to n-1
        
# left roate by k = 3
          # [1, 2, 3, 4, 5, 6, 7]
#         # [3 2 1 7 6 5 4]
#         # [4 5 6 7 1 2 3]

        
            
  

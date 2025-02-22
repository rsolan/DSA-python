https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m1 - bruteforce - merge 2 into ans arr , then copy ans in nums1

        # m3 - optimal

        if n ==0: return  #hadnling when n 0 nothing to merge seconfd matrx empty
        end = m+n-1
        i = m-1
        j = n-1
        while j>=0 and i >=0 :
            if nums1[i] <= nums2[j]:
                nums1[end] = nums2[j]
                j-=1
                end-=1

            else:
                nums1[end] = nums1[i]
                i-=1
                end-=1
        while j>=0: #handling frist mat empt
            nums1[end] = nums2[j]
            j-=1
            end-=1
        # print(nums1,nums2)


        # m2 - 

        # i = m-1
        # j = 0

        # while i>=00 and j <n:
        #     if nums1[i] > nums2[j]:
        #         nums1[i],nums2[j] = nums2[j], nums1[i]
        #         # print(nums1,nums2)
        #         i-=1
        #         j+=1
        #     else:
        #         break
        # # print(nums1,nums2)

        # for i in range(m,m+n):
        #     nums1[i] = nums2[i-m]

        # nums1.sort()

        

        

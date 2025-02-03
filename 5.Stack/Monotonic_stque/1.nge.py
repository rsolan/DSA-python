# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans for nums1 - for each val in nums1 - find nge in nums2


        # use dict to store result

        res = {}
        st =[]
        n = len(nums2)
        for i in range(n):
            while st and nums2[st[-1]] < nums2[i]:
                top = st.pop()
                res[nums2[top]] = nums2[i]
            st.append(i)

        # el left in stack - who doesnt have nge --- imp
        while st:
            top = st.pop()
            res[nums2[top]]  = -1
        
        out =[]
        # find ans for num1 only
        for i in nums1:
            out.append(res[i])

        return out


# https://leetcode.com/problems/next-greater-element-ii/description/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:


    #     0 1  2  3 4
    #     [1,2,3,4,3]
    # res=[2 3 4 ]

    #     st =  [ 3 , 4 ]

    #     [ 5 4 3 2 1]
          
    #       st = 5 4 3 2 1 

        #   if greater element doesnt exist - find again in the loop 

        st =[]
        n = len(nums)
        res=[-1 for i in range(n)]
        
        for i in range(2*n):   #-imp 2n
            # if i >=n: - i can revolve around - circularly
            i = i%n
            # print(i)

            while st and nums[st[-1]] < nums[i]:
                res[st.pop()] = nums[i]

            st.append(i)

        return res

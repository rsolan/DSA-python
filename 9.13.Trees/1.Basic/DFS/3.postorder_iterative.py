https://leetcode.com/problems/binary-tree-postorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # # m1 - recursive
        # def postorder(node):
        #     if node is None:
        #         return
        #     postorder(node.left)
        #     postorder(node.right)
        #     o.append(node.val)
            
        # # (L R ROOT)
        # o=[]
        # postorder(root)
        # return o

        # # m2.1 - 2 stacks:  -iterative , TC - O(N) , SC - O(2N)
        # # st1: by default root
        # # st2 - pop top of st1, put in st2, put top.left/right back in st1
        # # continue til lst1 empty , ans is reverse of st2 
        # st1 =[]
        # st2=[]
        # ans=[]
        # if root is None: #---- donet forget this case
        #     return ans
        # st1.append(root)
        
        # while st1:
        #     node = st1.pop()
        #     st2.append(node.val)
        #     if node.left:
        #         st1.append(node.left)
        #     if node.right:
        #         st1.append(node.right)

        # ans = st2[::-1] #reverse pf st2
        # return ans


        # M3 - Iterative - 1 stack TC - O(2N) SC - O(N)
        # Iterative Postorder - 1 Stack
        # TC: O(N)
        # SC: O(N)

        
        st = []
        curr = root
        ans = []

        while st or curr:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                temp = st[-1].right

                # if right subtree exists -> traverse it
                if temp:
                    curr = temp
                else:
                    temp = st.pop()
                    ans.append(temp.val)

                    # check if we came from right child
                    while st and temp == st[-1].right:
                        temp = st.pop()
                        ans.append(temp.val)

        return ans


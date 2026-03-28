# https://leetcode.com/problems/binary-tree-preorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # m1 -recursion
        # def preorder(node):
        #     if node is None:
        #         return   
        #     output.append(node.val)
        #     preorder(node.left)
        #     preorder(node.right)

        # # we traverse the BT in preorder fashion (ROOT L R) and we store in output instead of print
        # output=[]
        # preorder(root)
        # return output

        # m2 - iteration

        # 1.stack - by default - root placed
        # 2. push R then L -> so stack : [R,L,TOP] -> process L first 

        stk=[] # stack is mere a list as append and pop from back/top
        ans=[]
        if root is None:  # imp edge case
            return ans
        stk.append(root)

        while stk:
            top= stk.pop()
            ans.append(top.val)

            if top.right:
                stk.append(top.right)
            if top.left:
                stk.append(top.left)

        return ans



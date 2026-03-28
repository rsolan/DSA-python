https://leetcode.com/problems/binary-tree-inorder-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # m1 - recursive
        # def inorder(node):
        #     if node is None:
        #         return
        #     inorder(node.left)
        #     o.append(node.val)
        #     inorder(node.right)

        # # (L ROOT R)
        # o=[]
        # inorder(root)
        # return o

        # m2 - iterative
        # 1 null -> noede: pop stack top -> add node to ans -> go to node.right 
        # 2 not nul - go to left and keep pushing in stack

        ans =[]
        if root is None:
            return ans
        node = root
        stk=[]
        while True:
            if node is not None:
                stk.append(node)
                node=node.left
            else:
                if not stk:  #since stack is list - u cant cehck with `if stk is None`:
                    break

                node = stk.pop()
                ans.append(node.val)
                node = node.right
        return ans

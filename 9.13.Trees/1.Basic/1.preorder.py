# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node):
            if node is None:
                return   
            output.append(node.val)
            preorder(node.left)
            preorder(node.right)

        # we traverse the BT in preorder fashion (ROOT L R) and we store in output instead of print
        output=[]
        preorder(root)
        return output





'''
old:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root):
            if root is None:
                return
            # if not root:
            #     return

            o.append(root.val)
            preorder(root.left)
            preorder(root.right)

        o=[]
        preorder(root)
        return o
'''

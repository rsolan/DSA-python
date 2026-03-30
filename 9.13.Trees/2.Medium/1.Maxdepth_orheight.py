https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # m1 - max height/depth

        # recursive

        def findheight(node):
            if node is None:
                return 0

            lh = findheight(node.left)
            rh = findheight(node.right)
            return 1 + max(lh,rh)

            
        return findheight(root)




'''
old:


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # m1 -use recurive traversal to get depth , TC- O(N), SC - O(N) when skewed (not freq) -- better
        def recursive(root):
            if not root:
                return 0

            ans = 1 + max(recursive(root.left), recursive(root.right))
            returån ans

        return recursive(root)
        # m2 - use lvel order traversal - need queue SC - O(N)
'''

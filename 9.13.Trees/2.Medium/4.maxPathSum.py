https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def findheight(node):
            nonlocal maxi
            if not node:
                return 0

            # if any node return neg path sum - take 0  as why take that node in maxpathsub (need not to cver leaf/or al node in that path)
            # lh = findheight(node.left)
            lh = max(0,findheight(node.left))
            rh = max(0,findheight(node.right))

            maxi = max(maxi,lh+rh+node.val)

            # what will a node send back to its root - > take maxpathsum from any one l/r
            return node.val + max(lh,rh)

        # maxi =0 -- wrong max sum can be neg too
        maxi = -float('inf')
        findheight(root)
        return maxi
            














'''
old:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def recursivesum(root):
            nonlocal maxi
            if not root:
                return 0
            # ls = recursivesum(root.left)
            # rs = recursivesum(root.right)

            # Ignore negative paths by taking max with 0
            ls = max(0, recursivesum(root.left))  
            rs = max(0, recursivesum(root.right)) 
            
            maxi = max(maxi,root.val+ls+rs)
            ans = root.val + max(ls,rs)   #--impsteps , for any subnode - eith take ls or rs which is max as can take only 1 path
            return ans

        maxi = -float('inf')
        recursivesum(root)
        return maxi

'''

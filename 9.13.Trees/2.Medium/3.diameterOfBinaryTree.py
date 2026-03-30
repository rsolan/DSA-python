https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # m1 -

        def findheight(node):
            if node is None:
                return 0

            lh = findheight(node.left)
            rh = findheight(node.right)
            return 1 + max(lh,rh)

            
        def checkbalance(node):
            nonlocal maxi  # Allows modification of the outer 'maxi'
            if not node:
                return 0

            leftheight = findheight(node.left)
            rightheight = findheight(node.right)

            maxi = max(maxi,leftheight+rightheight)

            leftcall = checkbalance(node.left)
            rightcall = checkbalance(node.right)
            
            return maxi

        
        maxi=0
        checkbalance(root)
        return maxi





        # # m2 - while finding height - also check 
        # #  for each node =find the max curve it can form === lh+rh
        # #  keep updating teh maxi

        # maxi = 0

        # def findheight(node):
        #     nonlocal maxi #imp if wedontwant to pass maxi as diff arg
        #     if not node:
        #         return 0

        #     lh = findheight(node.left)
        #     rh = findheight(node.right)

        #     maxi = max(maxi,lh+rh) #store maxi height for each node
        #     #  but what to return to its root - max heigh out of l/r
        #     return 1 + max(lh,rh)
        
        # findheight(root)
        # return maxi


        # m3 - same as m2 just use maxi as arg -> use maxi as list as int are immutable

        

























'''
old:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # m2 - use height recursive fun directly
        # def recursive(root,maxi):
        #     if not root:
        #         return 0
        #     lh = recursive(root.left,maxi)
        #     rh = recursive(root.right,maxi)
        #     maxi[0] = max(maxi[0],lh+rh)
        #     ans = 1 + max(lh,rh)
        #     return ans

        # maxi = [0] #int are immutable so pass the list - or use 
        # recursive(root,maxi)
        # return maxi[0]

        # M3 - 
        def recursive(root):
            nonlocal maxi
            if not root:
                return 0
            lh = recursive(root.left)
            rh = recursive(root.right)
            maxi = max(maxi,lh+rh)
            ans = 1 + max(lh,rh)
            return ans

        maxi = 0
        recursive(root)
        return maxi

        # m1 - TLE 
        # def recursive(root):
        #     if not root:
        #         return 0

        #     ans = 1 + max(recursive(root.left), recursive(root.right))
        #     return ans

        # def diameter(node):
        #     nonlocal maxi  # Allows modification of the outer 'maxi'

        #     if not node:
        #         return

        #     lh = recursive(node.left)
        #     rh = recursive(node.right)
        #     # print(maxi,lh+rh)
        #     maxi = max(maxi,lh+rh)   #- for each node
            
        #     # repeat for nodeleft and noderight
        #     diameter(node.left)
        #     diameter(node.right)
        #     return maxi

        # maxi = 0
        # diameter(root)
        # return maxi




'''

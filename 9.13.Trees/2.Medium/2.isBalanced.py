https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # # m1 - recursive O(n2)

        # # find l,r height for each node
        # # return maxi

        # def findheight(node):
        #     if node is None:
        #         return 0

        #     lh = findheight(node.left)
        #     rh = findheight(node.right)
        #     return 1 + max(lh,rh)

            
        # def checkbalance(node):
        #     if not node:
        #         return True

        #     leftheight = findheight(node.left)
        #     rightheight = findheight(node.right)

        #     if abs(leftheight - rightheight)>1:
        #         return False

        #     leftcall = checkbalance(node.left)
        #     rightcall = checkbalance(node.right)

        #     if not leftcall or not rightcall:
        #         return False
            
        #     return True

        

        # return checkbalance(root)


        # m2 - check bal while finding height at each node , and return -1 if notbalance

        def findheight(node):
            if not node:
                return 0

            lh = findheight(node.left)
            if lh == -1:
                return -1
            rh = findheight(node.right)
            if rh == -1:
                return -1


            if abs(lh-rh)>1:
                return -1

            return 1+ max(lh,rh)

        if findheight(root) == -1:
            return False
        else:
            return True

        return findheight(root)!=-1


















'''
old:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # for every node , height(left)-height(right) <=1
        # m2 - use only recrusive height fun - return h if balanced, otherwise return -1

        def recursiveheight(root):
            if not root:
                return 0
            hl = recursiveheight(root.left)
            hr = recursiveheight(root.right)

            if hl == -1 or hr == -1:
                return -1
            if abs(hl-hr) > 1:
                return -1
            
            ans = 1 + max(hl,hr)
            return ans

        return recursiveheight(root)!=-1

        # M1 - O(N2). -> o(nxn) -> for each node find hight - n node, n height
        # def recursiveheight(root):
        #     if not root:
        #         return 0

        #     ans = 1 + max(recursiveheight(root.left), recursiveheight(root.right))
        #     return ans

        
        # if not root:
        #     return True

        # find height for root - fr each node - o(n) t ofind height
        # hl = recursiveheight(root.left)
        # hr = recursiveheight(root.right)
        # if abs(hl-hr) >1:
        #     return False

        # repeat for l/r
        # l = self.isBalanced(root.left) # go and check other nodes -left/right
        # r = self.isBalanced(root.right)
        
        # if not l or not r:  # if any node gives false then false
        #     return False
        # return True

'''

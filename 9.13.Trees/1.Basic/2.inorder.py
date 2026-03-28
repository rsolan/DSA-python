https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            o.append(node.val)
            inorder(node.right)

        # (L ROOT R)
        o=[]
        inorder(root)
        return o








'''
old:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # m1 - recursive
        # o=[]
        # def inorder(root):
        #     if root is None:
        #         return
        #     # if not root:
        #     #     return
        #     inorder(root.left)
        #     o.append(root.val)
        #     inorder(root.right)

        # inorder(root)
        # return o


        # o=[]
        # stack =[]
        # cur = root
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur= cur.left
        #     cur = stack.pop()
        #     o.append(cur.val)
        #     cur = cur.right

        # return o


        # m3
        st= []
        cur = root
        ans =[]
        if not root:
            return ans

        while st or cur:
            while cur:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            ans.append(cur.val)
            cur= cur.right
        return ans

'''

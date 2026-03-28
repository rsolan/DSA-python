https://leetcode.com/problems/binary-tree-postorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            o.append(node.val)
            
        # (L R ROOT)
        o=[]
        postorder(root)
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def postorder(root):
        #     o=[]
        #     if root is None:
        #         return
        #     # if not root:
        #     #     return  
        #     postorder(root.left)
        #     postorder(root.right)
        #     o.append(root.val)

        # postorder(root)
        # return o

        # m2 - iterative - using 2 stack
        # if not root:
        #     return []
        # st1=[root]
        # st2=[]
        # while st1:
        #     cur = st1.pop()
        #     st2.append(cur.val)

        #     if cur.left:
        #         st1.append(cur.left)
        #     if cur.right:
        #         st1.append(cur.right)
        # return st2[::-1]

        # m3 - iterative - using 1 stack
        st=[]
        cur = root
        ans=[]
        while cur or st:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                temp = st[-1].right
                if not temp:
                    temp = st.pop()
                    ans.append(temp.val)
                    while st and temp == st[-1].right:
                        temp = st.pop()
                        ans.append(temp.val)
                else:
                    cur = temp
        return ans

'''

'''
TRAVERSAL

BFS:
  level-order  
DFS: 
  preorder,inorder,postorder


'''


https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # q = 3  9,20  15,7
        # ans = l ,l ,l = 3,  9,20,  15,7

        ans=[]
        if root is None:
            return ans
        q = deque()
        q.append(root) #push is append

        while q:
            curr_sizeq= len(q) #9,20
            curr_ansl=[] 

            for i in range(curr_sizeq):
                node=q.popleft() #pop from q -popleft
                curr_ansl.append(node.val) #store ans first as node pointer will change

                if node.left:
                    q.append(node.left) # q = empty,15
                if node.right:
                    q.append(node.right) #q=empty,7
            ans.append(curr_ansl)

        return ans






'''
old:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = deque()
        q.append(root)

        while q:
            l=[]
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                l.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(l)
        return ans



'''

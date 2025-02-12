https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # m2 - optimized - merge sort
        # split from mid (5-3,2) - 
        # base case - stop till single el - 
        # 1 2 3 4   5 6 7
        def middle_fun(h):
            slow = h
            fast = h
            fast = fast.next #3----imp step 
            while fast and fast.next:   #for even we watn first middle  od and even
                slow = slow.next
                fast = fast.next.next

            return slow


        def merge2sorted(first, second):
            # m2 - optimized - tc - o(n+n), sc - o(1)
            t1 = first
            t2 = second
            dnode = ListNode(-1)
            temp = dnode
            while t1 and t2:
                if t1.val<t2.val:
                    temp.next = t1
                    temp = temp.next   #or temp = t1
                    t1=t1.next
                else:
                    temp.next = t2
                    temp=temp.next   #or temp = t2
                    t2=t2.next

            # while t1:  -- no need of while loop -as just connect the 1st link onlu
            if t1:
                temp.next = t1
            else:
                temp.next = t2
            return dnode.next
        
        def fun(head):
            if not head or not head.next:
                return head

            mid = middle_fun(head)

            lefthead = head
            righthead = mid.next
            mid.next = None #-- imp to separate

            lefthead=fun(lefthead) #- storing back to same variable
            righthead=fun(righthead)

            return merge2sorted(lefthead,righthead)  #backtracking-- return 

        return fun(head)
        
        # bt and merge insorted way

        '''
        # m1 - nlogn, sc = o(n) for arr
        # traverse into arr - sort - arr back to list
        arr=[]
        temp = head
        while temp:
            arr.append(temp.val)
            temp =temp.next

        arr.sort()
        dnode = ListNode(-1)
        temp = dnode
        for i in arr:
            nn = ListNode(i)
            temp.next = nn
            temp = nn
        return dnode.next
        '''

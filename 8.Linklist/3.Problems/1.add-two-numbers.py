https://leetcode.com/problems/add-two-numbers/

# tc- o(n1+n2) sc - o(n

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode(-1)
        temp = dummynode
        carry = 0
        t1 = l1
        t2 = l2
        # use t1=l1 and t2=l2 insetad of l1 and l2
        while t1 or t2:
            sumj = carry #or sumj = 0
            if t1:
                sumj+=t1.val
                t1=t1.next

            if t2:
                sumj+=t2.val
                t2=t2.next
            # sumj+=carry
            carry = sumj//10
            newnode = ListNode(sumj%10)
            temp.next = newnode
            temp = newnode

        if carry:
            newnode = ListNode(carry)
            temp.next = newnode
            # temp = newnode

        return dummynode.next

            

        

https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # m1 - iterative tc - o(n), sc- o(1)
        # prev = None
        # temp = head

        # while temp:
        #     nextp = temp.next
        #     temp.next = prev
        #     prev = temp
        #     temp = nextp

        # return prev

        # m2 - recursive
        def rev(head):
            if not head or not head.next:
                return head
            newhead = rev(head.next)  #- it will store last ie 5
            # head is at 4 now
            front = head.next #ie front = 4.next = 5
            front.next = head # 5.next  = 4
            head.next = None  #4.next = none

            return newhead

        return rev(head)

https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # m1- find len and then mid node - o(n+n/2) ->2 pass
        # cnt = 0
        # temp = head
        # while temp:
        #     cnt+=1
        #     temp=temp.next

        # mid = cnt//2+1

        # temp = head
        # while temp:
        #     mid-=1
        #     if mid ==0:
        #         return temp #-- imp return temp node not mid val
        #     temp=temp.next

        # m2 - tortoise and hare algo

        slow = head
        fast = head
        while fast and fast.next:   #-- imp fast first 
        # fast for even(m2) , fast.next for odd 
            slow = slow.next
            fast = fast.next.next
        return slow

        # if want frist m1 - then do fast.next.next for even

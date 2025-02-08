https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/submissions/1536238951/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        # m1- find len and then mid node - o(n+n/2) ->2 pass
        # IMP - FOR MIDDLE NODE WE WANT 1 LESS so as to acees next link
        if not head or not head.next:
            return None #- in case of 0or1 node - delete the node itself
        cnt = 0
        temp = head
        while temp:
            cnt+=1
            temp=temp.next

        mid = cnt//2 #--imp

        temp = head
        while temp:
            mid-=1
            if mid ==0:
                break
            temp=temp.next
        
        # temp is standing at 1 less than mid
        temp.next = temp.next.next
        return head
'''
        # m2 - tortoise and hare algo

        if not head or not head.next:
            return None #- in case of 0or1 node - delete the node itself

        slow = head
        fast = head
        fast = fast.next.next   #-- imp fast take 1 fast step ealrier

        while fast and fast.next:   #-- fast.next first 
        # fast for even for even(m2) , fast.next for odd 
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head


https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # m2 -USE FAST AND SLOWPOINTER
        # 1. move fast pointer till n node
        fast = head
        # while fast:
        #     fast=fast.next
        #     n-=1
        #     if n==0:
        #         break
        for i in range(n):
            fast=fast.next

        if not fast:  #- in case n = 5 , fast reaches none
            head = head.next
            return head

        # 2. then move slow and fast pointer both- slow pointer will be at 3
        slow = head
        while fast.next:
            fast = fast.next
            slow=slow.next

        # slow is at 3 pos
        slow.next=slow.next.next
        return head


        '''
        # m1 - nth node from end is  TC - O(LEN) + O(LEN-N) TRAVERSE LEN AND THEN DEL IT
        # -> move temp till res = total len-n
        #1 2 3 4 5
        #  del n = 2 ie delelte 4 nod
        #  from front move temp till res = len -n = 5-2 = 3 ie 3 node

        temp = head
        cnt = 0
        while temp:
            cnt+=1
            temp = temp.next

        res = cnt-n
        
        if n == cnt: #- delete first node
            head = head.next
            return head

        temp = head
        while temp:
            res-=1
            if res ==0:
                break
            temp = temp.next   #--- imp check when to move next - cant be done before res ==0 statement

        # print(temp)
        temp.next = temp.next.next
        return head
        '''

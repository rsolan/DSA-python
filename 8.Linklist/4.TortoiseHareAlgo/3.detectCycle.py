https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        # m1- use map to store NODE and not val and check if node repeats
        # TC - O(N) , SC - O(N)
        d ={}
        temp = head
        while temp:
            if temp in d:
                return True
            d[temp] = 1
            temp =temp.next

        return False
        '''

        # m2 - use tortoise and hare algo - o(n)
        slow  = head
        fast = head
        while fast and fast.next:   #--------------imp condition to break if no cycle
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

        

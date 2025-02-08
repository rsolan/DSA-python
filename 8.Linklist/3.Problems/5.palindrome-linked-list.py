# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # M2 0 4*n/2 
        # find m1 not m2 using tortoise-hare algo (even) - stop  at not f.n.n.
        # find m for odd - stop at f.n

        # reverse r2 from slow.next (head) 

        # compare l1 (head to slow) and r2(reversed) - return true/false  -- sec reaches null

        # u can reverse again to make it orginal  ---imp

        def reverse_fun(head):
            prev = None
            temp = head

            while temp:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front

            return prev

        if not head or not head.next:
            return True

        # 1. find mid - mid is at slow
        slow = head 
        fast = head
        while fast.next and fast.next.next:
            slow= slow.next
            fast=fast.next.next

        # 2. reverse from midnext to end
        reversehead = slow.next
        new_reversedhead = reverse_fun(reversehead)

        # 3. compare two ll - 1) head to slow , 2) new_reversedhead to non 
        # note l1 will be longer 
        #  123 21
        temp1 = head
        temp2 = new_reversedhead
        while temp2:  #as temp2 will be null first
            if temp1.val != temp2.val:
                return False  #-- u can reverse back the reversed ll
            temp1=temp1.next
            temp2= temp2.next

        return True




        



        '''
        # m1 - use stack lifo TC - O(2N) , SC - O(N)
        st =[]
        temp = head
        while temp:
            st.append(temp.val)
            temp= temp.next

        # print(st)
        temp = head
        while temp:
            topel = st.pop()
            if temp.val !=topel:
                return False
            temp= temp.next
        return True
        '''

        

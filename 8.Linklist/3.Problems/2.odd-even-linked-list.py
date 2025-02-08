# https://leetcode.com/problems/odd-even-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # m2 - optimized - O(N) SC - O(1)
        if not head or not head.next:
            return head

        evenhead = head.next
        odd = head
        even = head.next

        #-- as even will be ahead of odd and even will reach none first - NO NEED TO CHECK ODD IE 4 CONNECTED TO NON
        while even and even.next: 
            odd.next = odd.next.next #   1.NEXT - >3 , 1->3 , AND NEW ODD IS 3  (ODD IS ODD KA NEXT)
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = evenhead  #CONNECT 5 to 2
        return head

        '''
        # m1 - n/2+n/2+n - o(2n) , sc - o(n)
        t = head
        lis =[]
        # 0 - edge case
        if not head or not head.next:
            return head
        # 1. first pass
        while t and t.next:
            lis.append(t.val)
            t= t.next.next  #-- for this to work t and t.next cant be none as none.next - wrong

        if t: #for last node
            lis.append(t.val)
 

        # 2. second pas
        t  = head.next
        while t and t.next:
            lis.append(t.val)
            t= t.next.next

        if t: #for last node
            lis.append(t.val)

        # print(lis) - [1,3,5,2,4]
        # 3. udpate list val to original ll
        temp = head
        i = 0
        while temp:
            temp.val = lis[i]
            temp=temp.next
            i+=1

        return head
        '''

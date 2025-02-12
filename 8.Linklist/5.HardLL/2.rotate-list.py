https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k multipe of n - 
        # k>n
        # update tail and head link


        
        if not head or k==0: #- edge case
            return head
            
        tail = head
        cnt =1
        while tail.next: #--imp since we want last el also - to connect tail with head - so NOT use temp.
            cnt+=1
            tail = tail.next

        if k%cnt ==0:
            return head

        tail.next = head #---connect las to firs
        k = k%cnt

        tr = cnt - k
        newlastnode =head
        while tr:
            tr-=1
            if tr ==0:
                break
            newlastnode = newlastnode.next

        head = newlastnode.next #--- imp to update head first
        newlastnode.next = None

        return head

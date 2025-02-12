https://leetcode.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # temp = head
        # if less than k - cant reverse
        # for first k group - update the head

        # temp      k   
        # 1    2    3 -null ,  4   5   6  - null ,  7  8 

        #  3 2 1 ->4
        #  h   t

        #           t   k  nn
        #  3 2 1 -> 4 5 6->7
        #      p


        #                  t      k  nn
        #  3 2 1 -> 6 5 4->7  8  9 -> 10 11
        #               p

        # 1.break the kth link null (preserve k+1node) 
        # 2.- reverse the ll - reverse(temp) -- return reversedhead
        # 3. update the head to reversedhead for first itr
        # 3.for rem itr - connect reversedhead (6) to last node (1 - remem this as prev)
        # 4. connect temp to k+1 and repeat
        def reverse(t):
            pre = None
            while t:
                nn = t.next
                t.next = pre
                pre = t
                t = nn
            # return pre

        def findkthnode(t,k):
            t1= t
            while t1:
                k-=1
                if k ==0:
                    break
                t1=t1.next

            return t1

        temp = head
        while temp:                     
            kthnode = findkthnode(temp,k)

            if not kthnode: #less than k nodes
                if prevnode:  #- check when no prevnode - when just <k el liek only 2 el in total
                    prevnode.next = temp  #just ocnnect last temp to nextnode - noneed of reverse
                break

            nextnode = kthnode.next

            # reverse
            kthnode.next = None  #- brek the kthnode
            reverse(temp)

            temp.next = nextnode

            if temp == head:
                head = kthnode  #- first time
            else:
                prevnode.next = kthnode  #- this is to be done rem time

            prevnode = temp
            temp = nextnode

        return head






















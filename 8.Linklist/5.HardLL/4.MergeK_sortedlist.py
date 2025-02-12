https://leetcode.com/problems/merge-k-sorted-lists/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # m1 - traverse all list - arr - sort arr - convert arr into list ->nlogn and space



        # m2 - merge 2 list - then take that as new list and ocntinue till k list - n3 
        def sortTwoLists(first, second):
            # m2 - optimized - tc - o(n+n), sc - o(1)
            t1 = first
            t2 = second
            dnode = ListNode(-1)
            temp = dnode
            while t1 and t2:
                if t1.val<t2.val:
                    temp.next = t1
                    temp = temp.next   #or temp = t1
                    t1=t1.next
                else:
                    temp.next = t2
                    temp=temp.next   #or temp = t2
                    t2=t2.next

            # while t1:  -- no need of while loop -as just connect the 1st link onlu
            if t1:
                temp.next = t1
            else:
                temp.next = t2
            return dnode.next

        if len(lists)==0:
            return None  #-----imp edge caes - return none and not lists or []
        
        head = lists[0]
        for i in lists[1:]:
            head = sortTwoLists(head,i)

        return head



        # m3 - USE MIN HEAP  
        # tc - -> KLOGK+3KNLOGK  ~ n2 - optimal
        # sC- O(K) for heap
        
        # min heap = (val,node ) 
        heap =[]
        for i in lists: #klogk
            heapq.heappush(heap,(i.val,i)) #- store head.data,head node

        dnode = ListNode(-1)
        temp = dnode
        while heap: #kn elements x 3 operations of logk 
            minival,mininode = heapq.heappop(heap)
            temp.next = mininode
            temp =mininode
            if temp.next:  #---imp check when 1 ll becomes empty
                nextnode = temp.next
                heapq.heappush(heap,(nextnode.val,nextnode))

        return dnode.next

        

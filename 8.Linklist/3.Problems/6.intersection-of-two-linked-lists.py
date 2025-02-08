https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # m1 o(n+n) , sc - o(n)
        # traverse and store node and not val in dict for l1
        # check if any node ie c1 exist in dict while traversing for L2
        # return c1 or null if not

        # d={}
        # temp1 = headA
        # while temp1:
        #     d[temp1] = 1
        #     temp1=temp1.next
        
        # temp2 = headB
        # while temp2:
        #     if temp2 in d:
        #         return temp2

        #     temp2=temp2.next
        # return temp2


        '''
        # m2 - o(3n)
        # calcualte len n1 and n2
        # move longer one b upto d = n1-n2 
        # now l1 and l2 at same lvel
        # if equal - reurn tr
        # else false
        def fun(h1,h2,d):
            t1=h1
            t2= h2
            while d:
                t1=t1.next
                d-=1
            # now both ll on sme level
            while t1!=t2: #--IMP COND
                t1=t1.next
                t2=t2.next
            return t1

        temp1 = headA
        temp2= headB
        len1,len2=0,0
        while temp1:
            len1+=1
            temp1=temp1.next
        while temp2:
            len2+=1
            temp2=temp2.next
        if len1>len2:
            return fun(headA,headB,len1-len2)
        else:
            return fun(headB,headA,len2-len1)
            '''

        # m3  - o(n+n)
        # move t1 till null , then move t1 to head2 -> same for t2
        # now chceki both same , if both reaches to nul stop

        if not headA or not headB:
            return None #- if any of them is null - then intersection pooint is none
        t1 = headA
        t2= headB
        while t1!=t2:  #-- imp edge cas when both are same standning on 1st node
            t1=t1.next
            t2=t2.next

            if t1==t2: #- it wil return c1 or none
                return t1

            if not t1:
                t1 = headB
            if not t2:
                t2= headA

        return t1 #- edeg case 2 - when first node is same and t1=t2

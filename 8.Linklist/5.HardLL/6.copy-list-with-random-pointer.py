https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # m2 - optimizing the hasmap space 
        # tc - o(3n) , sc - o(n)for creating new ll which is mandatory
        # store temp in btw 2 nodes

        # 1. insert copynodes in btw 
        #  7  13
        # 7 13 11
        # 7-7-13-13-11
        temp = head
        if not head: #---e deg case
            return temp
        while temp:
            copy_node = Node(temp.val)
            copy_node.next = temp.next  #- preserve this first
            temp.next = copy_node
            temp = temp.next.next  #-moving 2 steps 

        # 2. for temp , copynoe is temp.next - coonect random pt of temp - but perofrm this action for copynode
        temp = head
        while temp:
            rp = temp.random
            copynode = temp.next
            if rp:
                copynode.random = rp.next #---imp as we want to point copy of random pointer ->temp.random.next
            else:
                copynode.random = None  #-- imp edgecase
            
            # temp.next.random = temp.random.next

            temp = temp.next.next

        # 3. connect next pointer , now copynode next belongs to next of temp
        # but we want to connect temp copynode to temp.next copynode
        temp = head
        head = temp.next
        while temp:
            copynode = temp.next
            nextnode = temp.next.next
            if nextnode:
                copynode.next = nextnode.next

            temp = nextnode
        return head



        '''
        # m1
        # tc - n +n 
        # sc - n for dict , n for new ll - which is reqd in quest to create

        # Traverse the ll - > store in dict - <original,copy> node address not value
        # traverse again in ll -> then join next and random pointers
        #  7 next point to copy of 13 and 
        #  7 random points to copy of null 

        
        
        temp  =head
        if not head: #---e deg case
            return temp
        d ={}
        while temp:
            copy_node = Node(temp.val)
            d[temp] = copy_node
            temp = temp.next
        print(d)

        temp = head

        while temp:
            copynode = d[temp]

            # copynode.next = d.get(temp.next, None)  # ✅ Fix: Use `.get()` to avoid KeyError
            # copynode.random = d.get(temp.random, None)  # ✅ Fix: Use `.get()` to avoid KeyError
         
            if temp.next:
                copynode.next = d[temp.next]
            else:
                copynode.next = None

            if temp.random:
                copynode.random = d[temp.random]
            else:
                copynode.random = None

            temp = temp.next

        return d[head]  #== imp 

        '''

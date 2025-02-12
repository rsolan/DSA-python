https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=remove-duplicates-from-a-sorted-doubly-linked-list

class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        
        # M1 - SORTED - o(n)
        temp = head
        while temp and temp.next:  #temp.next for nextnode
            nextnode = temp.next
            while nextnode and nextnode.data == temp.data:
                nextnode = nextnode.next
            
            # change the link
            temp.next = nextnode  #tempnext cna be null
            if nextnode:   #nextnode means nul have no prev 
                nextnode.prev = temp
            
            temp = nextnode  #or temp = temp.next
            
        return head

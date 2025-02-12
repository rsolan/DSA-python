https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-pairs-with-given-sum-in-doubly-linked-list


class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        '''
        # m1 - take help of sorted bth form head  - TLE
        
        out=[]
        temp1 = head
        while temp1:
            temp2 = temp1.next
            while temp2 and temp1.data+temp2.data <= target: #- no need to traverse if sum>target as sorted
                if temp1.data+temp2.data == target:
                    out.append((temp1.data,temp2.data))
                temp2= temp2.next
                
            temp1=temp1.next
            
        return out
        '''

      
        # m2 - dll is sorted - use 2 pointers from head and tail
        temp = head
        while temp.next:
            temp=temp.next #- reach temp till tail
        
        temp1 = head
        temp2 = temp
        out =[]
        while temp1.data<temp2.data:
            if temp1.data+temp2.data == target:
                out.append((temp1.data,temp2.data))
                temp1 = temp1.next #-- imp to mve frwrd both
                temp2 = temp2.prev
            elif temp1.data+temp2.data < target:
                temp1 = temp1.next
            else:
                temp2 = temp2.prev  #------prev not next
                
        return out

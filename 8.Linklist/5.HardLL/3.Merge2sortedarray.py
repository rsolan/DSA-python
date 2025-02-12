https://www.naukri.com/code360/problems/merge-two-sorted-linked-lists_800332?utm_source=youtube&utm_medium=affiliate&utm_campaign=Codestudio_Linkedlistseries&leftPanelTabValue=SUBMISSION

'''
    Following is the linked list node structure:
    '''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def sortTwoLists(first, second):
    # m2 - optimized - tc - o(n+n), sc - o(1)
    t1 = first
    t2 = second
    dnode = Node(-1)
    temp = dnode
    while t1 and t2:
        if t1.data<t2.data:
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

    '''
    # m1 = traverse 2 list into arr - sort them - put them back in list
    # tc - n+n+nlogn + n
    # sc - 2n
    arr=[]
    temp1 = first
    while temp1:
        arr.append(temp1.data)
        temp1=temp1.next

    temp2 = second
    while temp2:
        arr.append(temp2.data)
        temp2=temp2.next
    
    arr.sort()

    dummynode = Node(-1)
    temp = dummynode
    for i in arr:
        nn = Node(i)
        temp.next = nn
        temp = nn

    return dummynode.next
    '''

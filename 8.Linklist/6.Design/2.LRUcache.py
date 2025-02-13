https://leetcode.com/problems/lru-cache/

# Definition for a Node. -- u have to do this
class Node:
    def __init__(self, key: int, value: int):
        self.key = key  #---key is imp to del from dict
        self.val = value
        self.prev = None
        self.next = None
        
class LRUCache:
    def insertathead(self,currnode):
        nnode = self.head.next
        self.head.next =currnode
        currnode.prev = self.head
        currnode.next = nnode
        nnode.prev = currnode

    def deletenode(self,currnode):
        prevnode = currnode.prev
        nextnode = currnode.next
        prevnode.next = nextnode
        nextnode.prev = prevnode

    def __init__(self, capacity: int):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d={}  #d[key] = node
        self.capacity = capacity

    def get(self, key: int) -> int:
        # imp note - getting a node - makes it recently used 
        if key in self.d:
            currnode = self.d[key]
            self.deletenode(currnode)
            self.insertathead(currnode)
            return currnode.val  
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d: #1.update
            nn = self.d[key]
            nn.val = value  #onlu update val , since same node so dict key, node remain same

            self.deletenode(nn)
            self.insertathead(nn)

        else: #2.deleet or not and insert
            if len(self.d) == self.capacity:  # delete the LRU (from tail) and then put
                delnode = self.tail.prev
                del self.d[delnode.key]
                self.deletenode(delnode)

            nn = Node(key,value)  #- node has value
            self.d[key] = nn    #- dict has key and node
            self.insertathead(nn)





        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
cap
get the val - and put it in currently used
update/insert the key-val ; - isnert in current , update in current
if cap :- delete the LRU -- 

imp - if u get/putupdate somthing that become currently used
'''
# 
'''
implement
use doublw ll (key,val) and map dict(key,address)
dll insert towards heads and remvo from tail

get - check in map if exist , if not return -1
    if exist - delete the current node and insert same node in head (as it become mru) as have to keep track of LRU


put
1. exist allready - udpate 
            delete the node , isnert same node n front (since same node so no need to update in map)
2. else

    <cap - simpley insert at head
    cap exceeded -->
        deleete node from tail - ie tail.prev , also del it from map
        ceate new nde
        iserrt the new nde in front head and udpate in map
'''

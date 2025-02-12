https://leetcode.com/problems/design-browser-history/

# Definition for a Node. -- u have to do this
class Node:
    def __init__(self, x: str, next: 'Node' = None, prev: 'Node' = None):
        self.val = x
        self.next = next
        self.prev = prev
        
class BrowserHistory:

    def __init__(self, homepage: str): #o(1)
        self.current = Node(homepage)

    def visit(self, url: str) -> None: #o(1)
        nn = Node(url)
        self.current.next = nn
        nn.prev = self.current
        self.current = nn

    def back(self, steps: int) -> str: #o(steps)
        while steps:
            if self.current.prev:
                self.current = self.current.prev
            else:
                return self.current.val  #- when there is no back , traverse till the homepage
            steps-=1
        return self.current.val
        

    def forward(self, steps: int) -> str: #o(steps)
        while steps:
            if self.current.next:
                self.current = self.current.next
            else:
                return self.current.val  #- or just break
            steps-=1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

'''
decide ds
visiting a new page - length not defined so arr cant be used
back/forward - arr cant be used - as not pop we have to store them
cant use singly ll - as have to travrse in both dir

doubly ll - data is str url , next and prev ptr
'''

# recursion -> when a fun cal itself ultil a specifie cond is met - base cond
# stack space - where remaining non completed fun resides
# stack overflwo - segmentation fault

# recrusion tree
# depth of recursion


# TC - O(N)
# SC- O(N) 

def print5(i,n):
    if i>n:
        return
    print('name')
    print5(i+1,n)

n = 5
# print5(1,n)

def linear(i,n):
    if i>n:
        return
    print(i)
    linear(i+1,n)

count = 6
# linear(1,count)


def linearN1(i,n):
    if n<i:
        return
    print(n)
    linearN1(i,n-1)

count = 6
# linearN1(1,count)


def linearN1(i,n):
    if i<1:
        return
    print(i)
    linearN1(i-1,n)

n = 6
# linearN1(n,n)

# backtracking

# PRINITNG 1 TO N 
def linearN1(i,n):
    if i<1:
        return
    linearN1(i-1,n) # reach til 1
    print(i)


n = 6
# linearN1(n,n)


# PRINITNG N TO 1 
def linear(i,n):
    if i>n:
        return
    linear(i+1,n) #reach till n then print
    print(i)


n = 6
linear(1,n)







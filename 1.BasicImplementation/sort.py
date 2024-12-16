
def isGood():
    # l1 =[10,2,3,4]
    # l2 = [20,30,40]
    # l1 = [1,2,3,4,4,5]
    # l2 = [1,5,7,9]

    l1 =  [-1,0,1]
    l2 =  [0,2,4,6,8,10,12]

    
    out=[]
    # merge 2 sorted array  - 2 pointer approach
    i = 0
    j =0
    n1 = len(l1)
    n2 = len(l2)
    while i < n1 and j < n2:
        if l1[i] < l2[j]:
            out.append(l1[i])
            i+=1
        else:
            out.append(l2[j])
            j+=1

    while i < n1:
        out.append(l1[i])
        i+=1
    while j < n2:
        out.append(l2[j])
        j+=1
    print(out)





isGood()

# [1, 1, 2, 3, 4, 4, 5, 5, 7, 9]

# sort the string 
# kl djs dsa

def isort():
    s = "ahidfd"
    l = sorted(s)
    "".join(l)
    print(l)
# isort()

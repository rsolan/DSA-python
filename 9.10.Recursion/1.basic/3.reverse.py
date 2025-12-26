
# reverse using itr - use i and j from 0 and n -->keep on swapping till they collide
# 2 pointer
def rev(l,r):
    if l>=r:   # > for even , = for odd
        return
    arr[l],arr[r] = arr[r],arr[l]
    rev(l+1,r-1)

arr = [1,2,3,2,4]
n = len(arr)
# rev(0,n-1)
# print(arr)

# 1 var
def rev1(i):
    n = len(arr)
    if i>=n//2:
        return
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    rev1(i+1)

arr = [1,2,3,2,4]
rev1(0)
print(arr)

# x 
def reverse(arr,i):
    n = len(arr)

    if i ==n:
        return
    reverse(arr,i+1)
    print(arr[i])

arr = [1,2,3,2,4]
# reverse(arr,0)


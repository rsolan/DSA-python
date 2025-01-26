
def bis_left(arr,t):
    # start with h = n , no = sign
    l =0
    h = len(arr)
    while l<h:  # - stop mostly at l==h
        m = (l+h)//2
        print(l,h,m)
        if arr[m]<t:
            l = m+1
        else:
            h = m

    return l

def bis_right(arr,t):
    l =0
    h = len(arr)
    while l<h:
        m = (l+h)//2
        print(l, h, m)
        if arr[m]<=t:  #since i dont want = also  ,i want greater only
            l = m+1
        else:
            h = m
    return l


def bisect_left(arr,t):
    l  = 0
    n = len(arr)
    h = n-1
    ans = -1
    while l<=h:
        m = l+(h-l)//2
        if arr[m] == t:
            ans = m
            h = m-1
        elif arr[m] < t:
            l  = m+1
        else:
            h  = m-1

    if ans == -1:
        ans = l
    return ans

 # 0 1 2 3 4 5 6 7 8 9
# [1 2 2 3 5 6 6 6 7 8]
# bisect left
# bisect right

def bisect_right(arr, t):
    l = 0
    n = len(arr)
    h = n - 1
    ans = -1
    while l <= h:
        m = l + (h - l) // 2
        if arr[m] == t:
            ans = m
            l = m + 1
        elif arr[m] < t:
            l = m + 1
        else:
            h = m - 1

    if ans == -1:
        ans = l
        return ans
    else:
        return ans+1


if __name__ == '__main__':
    arr = [1,2, 2, 3, 5, 6, 6, 6, 7, 8]
    t = 6
    # bisect_right(arr,t)
    ans = bis_right(arr,t)
    print(ans)

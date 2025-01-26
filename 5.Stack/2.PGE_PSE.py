print('hi')



def prev_greater_element(arr):
    n = len(arr)
    st =[]
    res=[-1 for i in range(n)]
    for i in range(n-1,-1,-1):  #-- START FROM LAST INDEX
        while st and arr[st[-1]] < arr[i] :   #next arr[i] is greater so can be PGE
            index = st.pop()
            res[index] = arr[i]
        st.append(i)  #- imp stack has index not values

    return res


def prev_smaller_element(arr):
    n = len(arr)
    st =[]
    res=[-1 for i in range(n)]
    for i in range(n-1,-1,-1):
        while st and arr[st[-1]] > arr[i] :   #next arr[i] is smaller so can be PSE
            index = st.pop()
            res[index] = arr[i]
        st.append(i)  #- imp stack has index not values

    return res



arr = [2,1,5,3,6,8,3,5,4]
print(arr)
print(prev_greater_element(arr))
print(prev_smaller_element(arr))

# [2, 1, 5, 3, 6, 8, 3, 5, 4]
# [-1, 2, -1, 5, -1, -1, 8, 8, 5]
# [-1, -1, 1, 1, 3, 6, 1, 3, 3]





def next_greater_element(arr):
    n = len(arr)
    st =[]
    res=[-1 for i in range(n)]
    for i in range(n):
        while st and arr[st[-1]] < arr[i] :   #next arr[i] is greater so can be NGE
            index = st.pop()
            res[index] = arr[i]
        st.append(i)  #- imp stack has index not values

    return res


def next_smaller_element(arr):
    n = len(arr)
    st =[]
    res=[-1 for i in range(n)]
    for i in range(n):
        print(st)
        print(res)
        while st and arr[st[-1]] > arr[i] :   #next arr[i] is smaller so can be NSE
            index = st.pop()
            res[index] = arr[i]
        st.append(i)  #- imp stack has index not values

    return res



arr = [2,1,5,3,6,8,3,5,4]
print(arr)
# print(next_greater_element(arr))
# [2, 1, 5, 3, 6, 8, 3, 5, 4]
# [5, 5, 6, 6, 8, -1, 5, -1, -1]

print(next_smaller_element(arr))
#0  1 2   3  4  5  6  7  8
# [2, 1, 5, 3, 6, 8, 3, 5, 4]
# [1, -1, 3, -1, 3, 3, -1, 4, -1]



print('hi')



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

arr = [2,1,5,3,6,8,3,5,4]
print(next_greater_element(arr))
# [5, 5, 6, 6, 8, -1, 5, -1, -1]



'''
       0 1 2 3 4 5 6 7 8
arr = [2,1,5,3,6,8,3,5,4]
res = 

st = [0,1,]


       0 1 2 3 4 5 6 7 8
arr = [2,1,5,3,6,8,3,5,4]
res = [  5]

st = [0,]

       0 1 2 3 4 5 6 7 8
arr = [2,1,5,3,6,8,3,5,4]
res = [5 5 ]

st = []

       0 1 2 3 4 5 6 7 8
arr = [2,1,5,3,6,8,3,5,4]
res = [5 5 6 6   ]

st = [2,3,]
st = [2,]
st = []

      0 1 2 3 4 5 6 7 8
arr = [2,1,5,3,6,8,3,5,4]
res = [5 5 6 6 8-1 5 -1 -1  ]

st = [8 5 4]
st = [2,]
st = []
'''

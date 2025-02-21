
'''
*
**
***
****
****
***
**
*



def rec(i,n):
        if i ==n:
                print('*'*i)
                return
        
        print('*'*i)
        rec(i+1,n)
        print('*'*i)
    

rec(1,4)

def rec(i,n):
        if i ==n+1:
                return
        
        print('*'*i)
        rec(i+1,n)
        print('*'*i)
    

rec(1,4)


# def summ_dig1(n,s):
#         if n ==0:
#                 return

#         s[0] = s[0] + n%10
#         summ_dig(n//10,s)

# n  = 1234
# s = [0]
# summ_dig(n,s)

# print(s[0])

# def summ_dig2(n):
#         if n ==0:
#                 return 0

#         return n%10 + summ_dig(n//10)

# n  = 1234
# print(summ_dig(n))


# def sum_dig3(s):
#         if len(s)==0:
#                 return 0

#         return int(s[0]) + sum_dig(s[1:])

# n  = 1234
# s = str(1234)
# print(sum_dig(s)) #10

# reverse the dig using rec - > s = s *10 + (n%10)
''' 

# reverse a stack
# def reverse_stack(st,out):
#     if not st:
#         return 
    
#     out.append(st.pop())
#     reverse_stack(st,out)

# st = [1,2,3,4]
# out =[]
# reverse_stack(st,out)
# print(out)

# reverse using no extr apsce - extra insert call
# def insert(val,st):
#         if not st:
#                 st.append(val)
#                 return
#         # 1[]
#         # 2 [1] ->  [2,1]
#         #3 [2,1]  -> [321]
#         temp = st.pop()
#         insert(val,st)
#         st.append(temp)

# st = [1,2,3,4]
# def reverseij(st):
#         if st:
#                 val = st.pop()
#                 reverseij(st)

#                 insert(val,st)

# reverseij(st)
# print(st) - [4, 3, 2, 1]



# sort array in sam eway

def insert(val,st):
        if not st or st[-1]<val:  #7 [5,6] -> simple append -> [5,6,7]
                st.append(val)
                return
        # 6[]
        # 5 [6] -> pop 6 out , till empty of sec cond -> then insert 5 and then 6 [56]
        #3 [5,6]  -> []
        temp = st.pop()
        insert(val,st)
        st.append(temp)

st = [6,5,3,2,1]
def sort_array(st):
        if st:
                val = st.pop()
                sort_array(st)

                insert(val,st)

sort_array(st)
print(st)  [1, 2, 3, 5, 6]



# binary seq
# n = 3 ['000', '001', '010', '011', '100', '101', '110', '111']
# def rec(s,out,ind):
#         if ind ==n:
#                 out.append(s)  #immutables like string int are ok ,,  #list[:]
#                 return

#         rec(s+"0",out,ind+1)
#         rec(s+"1",out,ind+1)

# s = ""
# out = []
# rec(s,out,0)
# print(out)


# subseq
# s='ri' ['', 'i', 'r', 'ri']
# n = len(s)
# def subseq(s,out,ds,ind):
#     if ind == n:
#         out.append(ds)
#         return 
#     subseq(s,out,ds,ind+1)
#     subseq(s,out,ds+s[ind],ind+1)
    

# out =[]
# ds=""
# subseq(s,out,ds,0)
# print(out)

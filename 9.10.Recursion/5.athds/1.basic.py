# def calculateSpan(arr):
#         pass

# arr = [100 ,80, 60, 70, 60, 75, 85]
# calculateSpan(arr)


# def rec(ind,n):
#         if ind == n+1:
#                 return
#         print(ind)
#         rec(ind+1,n)
#         print(ind)
# n = 6
# # rec(1,n)

# def rec(ind):
#         if ind == 0:
#                 return
#         print(ind)
#         rec(ind-1)
#         print(ind)
# n = 6
# # rec(n)

# # forward prop, backward 


# def rec(ind,n):
#         if ind == n+1:
#                 return  #none
#         rec(ind+1,n)
#         print(ind)
# n = 6
# # rec(1,n)

# def summ(ind,s,n):
#         if ind == n+1:
#                 return s #-- only base should not return 
#         s=s+ind
#         return summ(ind+1,s,n)
#         # return summ(ind+1,s+ind,n)

# s= 0 
# n = 5
# # print(summ(1,s,n))

def fib(n):
        if n ==0:
                return 0
        if n ==1:
                return 1
        
        return fib(n-1)+fib(n-2) #2^N


# 0 1 1 2 3 5 8 13
# print(fib(7))

def fact(n):
        if n ==1:
                return 1
        
        return n * fact(n-1) # 1 rec cal 
n = 5
print(fact(n))

# branchcalls^n

# arr= [1,23,45,34,23]
# n = len(arr)

# def rev(out,ind):
#         if ind ==n:
#                 return

#         rev(out,ind+1)
#         out.append(arr[ind])

# out  =[]
# rev(out,0)
# print(out)


arr= [1,23,45,34,23]
n = len(arr)

def revs(i,j):
        if i>=j:
                return
        
        arr[i],arr[j] = arr[j],arr[i]
        revs(i+1,j-1)


revs(0,n-1)
print(arr)

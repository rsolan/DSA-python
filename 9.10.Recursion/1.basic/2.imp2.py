# parametrized

def summ(i,s):
    if i <1:
        return s
    return summ(i-1,s+i)


n = 3
# print(summ(n,0))



# functional 

def summ(n):
    if n == 0:
        return 0
    return n + summ(n-1)


n = 3
# print(summ(n))

def fact(n):
    if n==0 :  # or n ==1 
        return 1

    return n * fact(n-1)

print(fact(4))

# fib
def fib(n):
    # if n ==0:
    #     return 0
    # if n == 1:
    #     return 1
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)  #- 2 cals for n nos -> tc - 2^n

# TC - NO OF CALS^TOTAL EL - EXPONENTIAL



# 0 1 2 3 4 5 6 7  8
# 0 1 1 2 3 5 8 13 21

print(fib(8))

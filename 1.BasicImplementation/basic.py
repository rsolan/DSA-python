"""
Print Multiplication Table
Write a program to print the multiplication table for any number input by the user.

Odd or Even
Check whether a number entered by the user is odd or even.

Sum of a List
Create a function to calculate the sum of all elements in a list.

Simple Calculator
Write a calculator program that can add, subtract, multiply, and divide two numbers entered by the user.

Reverse a String
Take a string as input and print its reverse.

"""

def multiplication_table():
    inp = int(input("enter the number"))
    for i in range(1,11):
        print(f" {i} x {inp} = {i * inp}")

def check_oddeven():
    no = int(input("enter the number"))
    if no & 1:
        print(f"{no}  is odd")
    else:
        print(f"{no} is even")

def sum_list():
    lis = [1,2,3,4,50]
    sum = 0
    for i in lis:
        sum = sum + i
    print("sum of list = ", sum)

def calculator():
    a = int(input("enter first no : "))
    b = int(input("enter second no : "))

    print("""calculator, 
          1.addition
          2.subtarction
          3.multiplication
          4.division""")

    opt = int(input("press : 1,2,3 or 4 -> "))
    if opt == 1:
        print(a+b)
    elif opt == 2:
        print(a-b)
    elif opt ==3:
        print(a*b)
    elif opt == 4:
        if b == 0:
            print("cant divide with 0")
        else:
            print(a/b)
    else:
        print("wrong choice")


def reverse_string():
    inp_string = input(" ENTER A STRING TO REVERSE:")
    lis = list(inp_string)
    length = len(lis)
    nwlis=[]
    for i in range(length-1, -1, -1):
        nwlis.append(lis[i])
    print("".join(nwlis))

def reverse_string2():
    inp_string = input(" ENTER A STRING TO REVERSE:")
    print(inp_string[::-1])

# multiplication_table()
# check_oddeven()
# sum_list()
# calculator()
# reverse_string()
# reverse_string2()


"""
FizzBuzz
Print numbers from 1 to 100, but for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz." For numbers divisible by both, print "FizzBuzz."
Find the Largest Number
Take three numbers as input and find the largest among them.
Count Vowels in a String
Write a program that counts the number of vowels in a given string.
Check Palindrome
Write a function to check whether a given word is a palindrome (reads the same forward and backward).
Factorial of a Number
Write a function to calculate the factorial of a number using a loop.

"""


# 412 lc https://leetcode.com/problems/fizz-buzz/description/
def fizzBuzz():
    """
    :type n: int
    :rtype: List[str]
    """
    n = 5
    lis = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            lis.append("FizzBuzz")
        elif i % 3  == 0:
            lis.append("Fizz")
        elif i % 5 == 0:
            lis.append("Buzz")
        else:
            lis.append(str(i))
    print(lis)     

def greatest_threeno():
    a = int(input("enter first no : "))
    b = int(input("enter second no : "))
    c = int(input("enter third no : "))
    if a>b:
        if a>c:
            print(f"among {a} , {b} , {c} - {a} is greatest")
        else:
            print(f"among {a} , {b} , {c} - {c} is greatest")
    else:
        if b>c:
            print(f"among {a} , {b} , {c} - {b} is greatest")
        else:
            print(f"among {a} , {b} , {c} - {c} is greatest")

def greatest_threeno2():
    a = int(input("enter first no : "))
    b = int(input("enter second no : "))
    c = int(input("enter third no : "))
    if a>b and a>c:
        print(f"among {a} , {b} , {c} - {a} is greatest")
    elif b>c:
        print(f"among {a} , {b} , {c} - {b} is greatest")
    else:
        print(f"among {a} , {b} , {c} - {c} is greatest")




def count_vowel():
    inp = input("enter a string : ")
    count = 0
    for i in inp:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'): #TAKE CARE OF uppercase also
            count = count+1
    print(count)

def count_vowel2():
    inp = input("enter a string : ")
    vow = "aeiou"
    count = 0
    # vow = "aeiouAEIOU"
    for ch in inp:
        if ch.lower() in vow:
            count+=1
    print(count)
            


def check_palindrome():
    inp = input("enter a string to check pal : ")
    n = len(inp)
    flag = 1
    j = -1
    for i in range(0,n):
        if inp[i].lower() != inp[j].lower():
            flag = 0
            break
        j = j-1
        
    if flag:
        print(f" string =  {inp}  is palindrome")
    else:
        print(f" string =  {inp}  is NOT palindrome")

def check_palindrome2():
    inp = input("enter a string to check pal : ")
    inp = inp.lower()
    n = len(inp)
    for i in range(n//2):  # use of floor division n//2
        if inp[i] != inp[n-i-1]:  # imp ----------------- i sets for n-i-1
            return False
    return True



def factorial_loop():
    no = int(input("enter the no to calculate factorial : "))
    fact = 1
    if no == 0: # take care of edge case
        print(f"factorial of {no} is " , 1)
    else:
        for i in range(1,no+1):
            fact = fact * i
        print(f"factorial of {no} is " , fact)
        
        
# fizzBuzz()
# greatest_threeno()
# greatest_threeno2()
# count_vowel()
# count_vowel2()
# check_palindrome()

# if check_palindrome2():
#     print("string is palindrome")
# else:
#     print(" string is NOT palindrome")
# OP- 
# enter a string to check pal : raceCAR
# string is palindrome


# factorial_loop()


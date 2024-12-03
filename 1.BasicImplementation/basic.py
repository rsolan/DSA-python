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
    pass

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


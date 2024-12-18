

# Selection Bubble Insertion Merge Sort


#  n*n      n*n      n*n       n log n


# .sort() --> Merge Sort


# N log N --> N - length of the string


# Fixed Universe
# Numbers ---> -inf to inf
# Alpabets --> a -- z or A -- Z   # 26
# Printable Chars --> 256


# String is made up of characters
#  a b c d e f         z
# [3,2,1,2,2,0,........25th Index]  # 26
#     
# "debbacdaae"   # O(n+m)   where is the range  (0--26) 
# 
#


# aaabbcddee


# a -- 0    # ord(char)-97 == 0 -- 25
# b -- 1
# c -- 2
# ......


# A -- 0
# B -- 1    # ord(char)-65 == 0 -- 25


# All printable Character
# [0,0,0,0,.....256]
# 'a' -- 97
# 'A' -- 65
# '&' -- ascii value


# 1. Convert the string into a array dictionary
# 2. a--0 b--1 c--2
# 3. Traverse the array and construct your answer
# 4. 4 --> chr(4 + 97)
# 5. 2 --> chr(2 + 97) -- c


# 6. 256 directly map to its ascii value

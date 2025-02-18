https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # m1 - 
        # generate n! permutations - then return the kth permutation
        # n! x n to generate all permuation , n to store in arr, 
        # zlogz to sort all perm so that we can return kth perm ; here z = n!xn


        # m2 tc - o(n2)   n for calcalting fact , n for poping each time 
        # ,sc- o(n) n for arr or ans
        '''
        arr =[1,2,3,4]
        lets say n = 4 , k = 17
        4->4!= 24 0to23 we haev to return 16th perm as we are starting from 0
        so lets find the bin , instead of generating all
1)
        6 0 to 5         6  6 to 11      6 12 to 17      6 18 to 23
        startswith1     startswith2     startswith3     startswith4
        n = 4
        k =k//(n-1)! = 16//6 = 2 arr[2] = 3
        16th lie in 3rd bin so first char is _3  _ _ _

2)
        now zoom into 
        6 -> 12 to 17
        startswith3
        n = 3
        k = k %fact = 
        k =k//(n-1)! = 16//2 = 2 arr[2] = 3
        '''



        
        fact = 1
        arr=[]
        for i in range(1,n):  #not inc n as we want 1fact less - > as first group of 6 for 4!
            fact = fact*i
            arr.append(i)

        arr.append(n)
        # n = 4 , k = 17-1=16
        # print(fact,arr) 6  [1, 2, 3, 4]
        # ans = 3412
        ans=""
        k = k-1 #as start from 0
        while True:
            ans = ans + str(arr[k//fact])   #arr[16//6] = arr[2] =3 
            arr.pop(k//fact)   #pop 2nd index = 3 out

            if len(arr)==0: #now len is 4-1= 3 after removing 2nd index
                break

            k  = k %fact  #k = 16%6 = remainder= 4  
            # i want kth number ie 4th number ,next group of size =2  
            # old size = 6 for 3! 
            # new size = 2 for 3!/3
            fact = fact//len(arr) 

        return ans
            



























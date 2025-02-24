https://leetcode.com/problems/boats-to-save-people/
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # since can take max 2 - so use2pointers
        people.sort()
        n = len(people)
        i = 0
        j = n-1
        c=0
        while i <=j: #- take equla cse
            if people[i]+people[j] <=limit:
                c+=1
                i+=1
                j-=1
            else:
                c+=1
                j-=1  #why to take larger one and not smaller, sm can combine with other

        return c



        # sort 
        # [3,2,2,1]
        # 1 2 2 3

        # nlogn +n
# peoples weight > limit
        # 3 3 4 5
#             i
#             1

#             1 1 1 1 2 2 2 2
#             i             j
#                       3
#                       6 
# limit = 3

        # why 2 point - greedy 1 smaller 1 larger
        




https://leetcode.com/problems/backspace-string-compare/description/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        # Note that after backspacing an empty text, the text will continue empty.- empty string?

        # ab#c##d
        #  i
        #  2
        

        # as#d
        #     j
        # m1 - 2 pointers
        def countf(s):
            n = len(s)
            c = 0
            ans =""
            for i in range(n-1,-1,-1):
                if s[i] == '#':
                    c+=1
                else:
                    if c>0:
                        c-=1
                    else:
                        ans+=s[i]
            return ans

        return countf(s) ==  countf(t)
        '''

        # m2- array - push and pop - O(n), extra space - o(n)
        l1 = []
        for i in s:
            
            if i =="#":
                if l1:
                    l1.pop()
                else:
                    l1=[]  #Note that after backspacing an empty text, the text will continue empty.
                    # break  ->dont break as it can continue
            else:
                l1.append(i)


        l2 = []
        for i in t:
            if i =="#":
                if l2:
                    l2.pop()
                else:
                    l2=[]
                    # break
            else:
                l2.append(i)

        return l1==l2

        





https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # go with profit 

        # 50 40 30 20 10
        # 10 8 6 4 2

        # worker sort

        n = len(profit)
        l =[]
        for i in range(n):
            l.append((profit[i],difficulty[i]))

        l.sort(key = lambda x:-x[0])
        print(l)
        # [(50, 10), (40, 8), (30, 6), (20, 4), (10, 2)]

        val = l[0][1] # max profit workd difficulty
        arr =[l[0]]
        # remove those who has more diffilcult and less profit 
        for i in range(1,n):
            if l[i][1] <= val:
                val = l[i][1]
                arr.append(l[i])

        worker.sort(reverse = True)
        print(arr)
        print(worker)
        # 7 6 5 4
        n1 = len(arr)
        n2 = len(worker)
        i = 0
        j = 0
        maxprofit = 0
        while j <n2 and i <n1:
            if arr[i][1] > worker[j] :
                i+=1
            else:
                maxprofit+=arr[i][0]
                j+=1

        return maxprofit









        

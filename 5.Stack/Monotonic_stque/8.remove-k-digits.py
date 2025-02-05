# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # edge case 
        # -1. k>n - remove al - return 0
        #  2.all small in stak - 12345 - remvoe k el from end
        #  3. remvoing leading 0s

        # larger el - at starting indexes

        # "1 432219"
        # st = [1 219 ]   - ans

        # "5 4 3 2 1" k = 2
        # st = [ 321 ] 


        # 1 4 2 5 6 3 1 9 k = 1
        #           i
        # st = [1 4  ]
        # st = [1 2 5  6]
        # st = [1 2 5 ]
        # st = [1 2 3]
             
        # st = [1 4 5 2]     ans - monotonic inc 
        n = len(num)
        # if n ==1:
        #     return '0'
        st = []
        for i in num:
            while k>0 and st and i < st[-1]:   #i want smaller i's in stack
                st.pop()
                k-=1

            st.append(i)

        while k>0:  #- if we have all inc follwoed by dec and i>n
            st.pop()
            k-=1

        print(st)
        st2 =[]
        no =0
        while st:
            top = st.pop()
            st2.append(top)
            no = no + int(top)
        if no ==0:
            return '0'
        while st2:
            if st2[-1] == '0':
                st2.pop()
            else:
                break
        print(st2)
        ans1 = "".join(st2)
        print(ans1)
        return ans1[-1::-1]


        # whiel st [0] == 0 - pop it 






        

# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # -5 -6 -7

    

        # [5,5,5,5,-15]

        # st = [5 5 5 (15,-1) ]

        
        #      [2 4 5 -10 2 2 -4 10]
       

        # st = [2 4 5 -10]
        #           b   a

        arr = asteroids
        st =[]
        for i in arr:
            st.append(i)  #- always
            while len(st)>1: #bcoz we want top 2
                a = st.pop()
                b = st.pop()

                if a<0 and b>0:
                    if abs(a)> abs(b):
                        st.append(a) #- add the greater one back
                    elif abs(a)< abs(b):
                        st.append(b)
                    else:
                        break #-- when both equal , already popped out
                else: #- rem 3 cases
                    st.append(b)
                    st.append(a)
                    break

        return st




        







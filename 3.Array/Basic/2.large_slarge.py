https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-element-in-array



class Solution:
    def largest(self, arr):
        # code here
   
        maxi = -1
        for i in arr:
            if i > maxi:
                maxi = i
                
        return maxi




https://www.geeksforgeeks.org/problems/second-largest3735/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=second-largest



class Solution:
    def getSecondLargest(self, arr):
        
        m = -1  #--not with 0 
        sm = m
        for i in arr:
            if i >m:
                sm = m
                m = i
            elif i>sm and i<m:
                sm = i
        return sm
        
        
        '''
        maxi=-1
        smaxi = -1
        for i in arr:
            if i> maxi:
                smaxi = maxi
                maxi = i
            # else: -- it include =case also 
            elif i<maxi and i>smaxi:
                    smaxi = i
                    
        return smaxi
                
        
        # Code Here
        
        # m1 - n + nlogn =  o(nlogn) - sort and then return 1st index element
        # arr.sort(reverse = True)
        # i = 1
        # while i<len(arr) and arr[i]==arr[0]:
        #     i+=1
        
        # if i == len(arr):
        #     return -1
        # else:
        #     return arr[i]




        # m2 - better = n+n = o(2n)
        # find largest , then find second largest
        
        
        # maxi=arr[0] #largest
        # for i in arr:
        #     if i>maxi:
        #         maxi = i
                
        # s= -1 #second largest - since all positive element, otherwise take it as int_min
        # for i in arr:
        #     if i >s and i!=maxi:
        #         s = i
                
        # return s
        
        
        
        
        # m3 - o(n)
        #find l and sl in 1 pass
        # arr = [124775]
        l=arr[0]
        sl = -1  # or tke -inf in case of negative elements also 
        for i in arr:
            if i>l:
                sl = l
                l=i
                # sl = l --- wrong do it before l , store l value before changin l
            elif i<l and i>sl:
                sl = i
        
        return sl
        
        
        # second smallest ??
        # s=arr[0]
        # ss = float("inf")
        # for i in arr:
        #     if i<s:
        #         ss = s
        #         s=i
                
        #     elif i!=s and i<ss:  #imp --> i!=s
        #         ss = i
        
        # return ss
        '''

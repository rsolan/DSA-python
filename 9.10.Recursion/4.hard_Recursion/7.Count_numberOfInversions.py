https://www.naukri.com/code360/problems/number-of-inversions_6840276?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems&leftPanelTabValue=PROBLEM

from typing import *

def numberOfInversions(arr : List[int], n : int) -> int:
    # Write your code here.
    # m1 - bruteforce - o(n2)
    # cnt  = 0
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if arr[i]>arr[j]:
    #             cnt+=1

    # return cnt
        

        # m2 - use mergesort - o(nlogn) , sc - n for temp arr
        # changing the arrayas makingit osrted  - u can make a copy of it if u dont want to distort it

        # arr = [5,3,2,4,1]

        # do merge sort - while merge sort when u r merging back check 
        # chck the cond if arr[i]>arr[j] - inc the cnt


        cnt  = [0] #->int cant be mutated - global var- not prefered
        def merge(l,mid,r,arr,cnt):
            left = l
            right = mid+1
            t=[]
            cnt1 = 0
            while left<=mid and right<=r:
                if arr[left] <= arr[right]:
                    t.append(arr[left])
                    left+=1
                else:
                    t.append(arr[right])
                    # cnt+=1 -- not inc by 1  here r less than l -> all l bigger than current r
                    # cnt[0]=cnt[0] + (mid-left+1)
                    cnt1=cnt1 + (mid-left+1)
                    right+=1
                    
            while left<=mid:
                t.append(arr[left])
                left+=1
                
            while right<=r:
                t.append(arr[right])
                right+=1
                
            for i in range(l,r+1):  
                arr[i] = t[i-l]

            return cnt1


        def mergesort(left,right,arr,cnt):
            cnt1 = 0
            if left>=right:
                # return
                return cnt1

            mid = (left+right)//2
            # mergesort(left,mid,arr,cnt)
            # mergesort(mid+1,right,arr,cnt)
            # merge(left,mid,right,arr,cnt)

            cnt1+=mergesort(left,mid,arr,cnt)
            cnt1+=mergesort(mid+1,right,arr,cnt)
            cnt1+=merge(left,mid,right,arr,cnt)
            return cnt1
            

        n = len(arr)
        left = 0
        right = n-1
        # mergesort(left,right,arr,cnt)
        # return cnt[0]
        return mergesort(left,right,arr,cnt)
        

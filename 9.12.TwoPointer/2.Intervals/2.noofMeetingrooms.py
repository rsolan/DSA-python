https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # inc when meeting starts, and dec when meeting ends
        # o(nlogn + n)
        s= []
        e =[]
        n  = len(intervals)
        for i in range(n):
            s.append(intervals[i][0])
            e.append(intervals[i][1])

        s.sort()
        e.sort()
        n1 = len(s)
        n2 =len(e)
        # print(s)
        # print(e)
        # INC THE ROOM IF MEETING STARTS , REDUCE THE ROOMS IF MEETING ENDS 
        c = 0
        i, j = 0,0
        maxi = 0
        while i<n1 and j <n2: #- why and as max c canbe equal to n
            if s[i] < e[j]:
                c+=1
                i+=1
            else:
                c-=1
                j+=1
            maxi = max(maxi,c) #- max uninterupted c
            
        return maxi








https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1


class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        # greedy 
        # intersecting
        TC- O(2N+2NLOGN)
        
        
        # min no of rooms such that no conflict
        # inc the count if train arrives
        # dec the count if train depart
        arr.sort()
        dep.sort()
        i,j=0,0
        c = 0
        n = len(arr)
        maxi = 0
        while i<n and j <n:  #while i<n will also work as arrival wil exhaust first
            if arr[i] <= dep[j]:
                c+=1 #inc the no of platform if train narrives
                i+=1
            else:
                c-=1
                j+=1
            maxi = max(maxi,c)
            
        return maxi
        # coinicidicing platform  - HANDLE = CASE  --IMP
        #                                                                                      i
        # Array a (sorted): 515 , 723 , 743 , 951 , 1025 , 1116 , 1143 , 1514 , 1525 , 1611 , 1729 , 1827 , 1835 , 2203 , 2225 
        #                                  j
        # Array d (sorted): 1049 , 1337 , 1611 , 1625 , 1633 , 1639 , 2003 , 2009 , 2149 , 2151 , 2153 , 2231 , 2252 , 2330 , 2352 

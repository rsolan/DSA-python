https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        points = list(zip(start,end))
        n = len(points)
        if n ==0:return True
        c=1
        points.sort(key = lambda x:x[1])

        s = points[0][0]
        e= points[0][1]
        for i in range(1,n):
            if points[i][0]>e:  
                c+=1
                e = points[i][1]

        return c
        
        # code here
        # max th meting no - min the s to e time
        # take meeting who ends faster - soert end
        '''
        
                  T       N     T
        [0,1],[1,2] [3,4] [3,7],[2,5],[0,6],[7,12],[13,15]
        
        Sort based on Ending Time
          S    S                                S        S
        [1,2] [3,4],[2,5],[0,6], [4,7],[7,12],[13,15]
                          C      C      C
        
        
        # Sorting by Ending → Greedy to choose Soon Ending Meetings → SO you maximize the number of meetings you hold
        

        # greedy - 
        # take meeting ending sooner
        n = len(start)
        l =[]
        for i in range(n):
            l.append([start[i],end[i]])
            
        l.sort(key = lambda x:x[1])
        #   T      T      N     N       N      T         T
        # [1,2] [3,4],[2,5],[0,6], [4,7],[7,12],[13,15]
        c =1
        s = l[0][0]
        e = l[0][1]
        for i in range(1,n):
            if l[i][0] > e:
                c+=1
                e = l[i][1]  #--update e only if u atke the meeting 
        return c
            # c here is count of non-overlapping , non - conflcit - can happen in 1 room 
            
            
        '''






https://leetcode.com/problems/meeting-rooms/

     class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        if n ==0:return True
        c=1
        intervals.sort(key = lambda x:x[1])

        s = intervals[0][0]
        e= intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]>=e:
                c+=1
                e = intervals[i][1]

        return c==n





https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        n = len(points)
        if n ==0:return True
        c=1
        points.sort(key = lambda x:x[1])

        s = points[0][0]
        e= points[0][1]
        for i in range(1,n):
            if points[i][0]>e:  #- IF EQUAL - THEN CAN BE SHOT TOGETHER , NOT CONCISDERED COLIDE FOR MEETIG
                c+=1
                e = points[i][1]

        return c

https://leetcode.com/problems/non-overlapping-intervals/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        # maxi non overlapping intervals c , mini overlapping intervals n-c
            # https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
        intervals.sort(key = lambda x:x[1])
        c =1
        s = intervals[0][0]
        e = intervals[0][1]
        for i in range(1,n):
            if intervals[i][0] >= e:  #- e can be same for non overlapping
                c+=1
                e = intervals[i][1]
        return n-c


        # C= 3 MEETINGS I CAN JOIN = NON OVERLAPPING 
        # SO REMOVE N-C MEETINGS = OVERLAPPING




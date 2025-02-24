https://leetcode.com/problems/insert-interval/
tc- o (n) , sc - o(n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # greedy L9
        # (merge overlapping intervals if necessary).

        i =0
        res=[]
        n = len(intervals)
        # STEP 1 - LEFT SIDE [[1,2]
        while i < n and intervals[i][1]< newInterval[0]:
            res.append(intervals[i])
            i+=1

        # STEP 2 new interval [4,8] overlaps with [3,5],[6,7],[8,10]. START I beofre newint ends
        # for those overlappingon e- take min and max index 3,6,8 before 8 ends
        while i<n and intervals[i][0] <= newInterval[1]:  #-- = is imp
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1

        res.append(newInterval)  #maake change in ni as there can be no 2nd loop

        # step3 - remaining add
        while i<n:
            res.append(intervals[i])
            i+=1

        return res

        


        # print(res)


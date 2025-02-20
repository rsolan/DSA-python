https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=who-will-win

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        # there can first occ -start from 0 , last occ - start from last ind, all occ - store all occ
        for i in arr:
            if i == k:
                return True
        return False

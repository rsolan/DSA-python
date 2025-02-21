https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        

        def rec(ind, arr,k):
            if len(arr) ==1:
                return arr[0]

            ind = ind + k - 1
            ind = ind% len(arr)
            arr.pop(ind)
            # print(arr)
            return rec(ind, arr, k  )
            
        
        arr = [i+1 for i in range(n)]
        return rec(0,arr,k)

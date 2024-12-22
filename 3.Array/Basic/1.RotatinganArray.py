# Left Rotate array by 1 place: https://www.naukri.com/code360/problems/left-rotate-an-array-by-one_5026278?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse&leftPanelTabValue=SUBMISSION
# Left Rotate array by D places: 
# Problem Link 1. https://www.geeksforgeeks.org/problems/reversal-algorithm5340/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=reversal-algorithm
# Problem Link 2. https://www.naukri.com/code360/problems/rotate-array_1230543?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems
# Right Rotate array by d places: https://leetcode.com/problems/rotate-array/description/

# 1. Left ROTATE BY 1
def LeftrotateArrayby1(arr: [], n: int) -> []:
    # Write your code from here.
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    
    arr[n-1] = temp
    return arr

# 2left rotate by k
# m1 - brute force TC - O(N+K) , SC - O(K)
def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    n = len(arr)
    l=[]
    k = k%n # for k >n say n = 7 , k = 20 , k= 20%7 = 6 
    for i in range(0,k):
        l.append(arr[i])
#                k       
# 'arr '= [1,2,3,4,5]
#          0 1 2 3 4
# arr =[4,5]

# [1, 2, 3]
# [4, 5, 3, 4, 5]
# [4, 5, 1, 2, 3]
    for i in range(k,n):
        arr[i-k] = arr[i]

    # for i in range(len(l)):
    #     arr[n-k + i] = l[i]
    j = 0
    for i in range(n-k,n):
        arr[i] = l[j]
        j+=1
    return arr



# M2 - OPTIMAL NO SPACE complexity  , TC - O(2N)
        # reverse first 0 to k-1 , reverse rem k to n-1 , reverse total 0 to n-1
class Solution:
    def reverse(self,arr,start,end):
        i=start
        j = end-1
        while i<=j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
            
        
    def leftRotate(self, arr, d):
        # code here
        
        n = len(arr)
        self.reverse(arr,0,d)
        self.reverse(arr,d,n)
        self.reverse(arr,0,n)
      


# 3. RIGHT rotate by k , LC MED 189
# m1 - same like left rotate , just made 1 full rotate before
class Solution:
    def reverse(self,arr,start,end):
        i=start
        j = end-1
        while i<=j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
            
        
    def leftRotate(self, arr, d):
        # code here
        
        n = len(arr)
        self.reverse(arr,0,n)
        self.reverse(arr,0,d)
        self.reverse(arr,d,n)
        


# m2
class Solution:
    def reverse(self,arr,start,end):
        i=start
        j = end-1
        while i<=j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        print(arr)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # k = 5 , n = 6
        # [1, 2, 3, 4, 5, 6]
        # [1, 6, 5, 4, 3, 2]
        # [2, 3, 4, 5, 6, 1]
        n = len(nums)
        k = k%n #imp
        self.reverse(nums,0,n-k)
        self.reverse(nums,n-k,n)
        self.reverse(nums,0,n)



        
            
  

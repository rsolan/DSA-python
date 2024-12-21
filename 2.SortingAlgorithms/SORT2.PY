class Solution:
    def merge(self,arr,l,mid,r):
        left = l
        right = mid+1
        t=[]
        while left<=mid and right<=r:
            if arr[left] <= arr[right]:
                t.append(arr[left])
                left+=1
            else:
                t.append(arr[right])
                right+=1
                
        while left<=mid:
            t.append(arr[left])
            left+=1
            
        while right<=r:
            t.append(arr[right])
            right+=1
            
        for i in range(l,r+1):  #??? why l to r+1 and why i-l
            arr[i] = t[i-l]
            
    def mergeSort(self,arr, l, r):
        #code here
        if l>=r:
            return
        mid = (l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)


class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low<high:
            partitionIndex = self.partition(arr,low,high)
            self.quickSort(arr,low, partitionIndex-1)
            self.quickSort(arr,partitionIndex+1,high)
    
    def partition(self,arr,low,high):
        # code here
        pivot = arr[low]
        i = low
        j = high
        while i < j:
            while arr[i] <=pivot and i<=high-1:
                i+=1
            
            while arr[j] > pivot and j >=low+1:
                j-=1
            
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]
                
        
        arr[low],arr[j] = arr[j],arr[low]
        return j
    

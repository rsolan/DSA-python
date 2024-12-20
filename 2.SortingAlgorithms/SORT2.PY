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

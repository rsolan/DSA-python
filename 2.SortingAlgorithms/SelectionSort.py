def selectionSort(self, arr):
        #code here
    
        

        n = len(arr)
        for i in range(0,n-1):   #or 0 to n also works
            
            mini = i   #mini is set as current indx itself - incase no other min
            for j in range(i,n):
                if arr[j] < arr[mini]:
                    mini = j
            arr[i],arr[mini] = arr[mini],arr[i] #swap
        return arr

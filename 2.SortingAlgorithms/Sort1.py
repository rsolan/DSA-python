


def selectionSort():
    # code here
    arr = [4,1 ,3, 9, 7]
    print(arr)
    n = len(arr)
    for i in range(0, n - 1):  # or 0 to n also works

        mini = i  # mini is set as current indx itself - incase no other min
        for j in range(i, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]  # swap
    print(arr)

def bubbleSort():
    # code here
    arr = [4,1 ,3, 9, 7]

    n = len(arr)
    for i in range(n - 1, 0, -1):
        swaped = False
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaped = True
        if not swaped:  # No swaps in this pass, array is sorted
            break
    print(arr)


def insertionSort():
    # code here
    arr = [4,1 ,3, 9, 7]

    n = len(arr)
    for i in range(0, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    print(arr)


if __name__ == '__main__':
    print_hi('PyCharm')
    # selectionSort()
    # bubbleSort()
    insertionSort()

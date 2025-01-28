def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
        if swapped == False:
            break
    return arr

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                swapped = True
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
        if swapped == False:
            break
    return arr
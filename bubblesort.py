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

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Sorted array in ascending:")
    bubble_sort_asc(arr)
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    print()        
        
    print("Sorted array in descending:")
    bubble_sort_desc(arr)
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
def insertion_sort_asc(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while j>=0 and key>arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Sorted array in ascending:")
    insertion_sort_asc(arr)
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    print()        
        
    print("Sorted array in descending:")
    insertion_sort_desc(arr)
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

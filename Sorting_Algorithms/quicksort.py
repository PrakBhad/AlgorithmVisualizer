import random


def swap(arr,i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

def quick_sort_asc(arr, low, high):
    if low < high:
        # Random Pivot
        pivot_Index = random.randint(low, high)
        pivot_Value = arr[pivot_Index]
        
        swap(arr,pivot_Index,high) #Swap Highest Index Value with the pivot
        i = low -1
        
        for j in range(low,high):
            if arr[j]<pivot_Value:
                i+=1
                swap(arr,i,j)
        
        swap(arr,i+1,high)
        quick_sort_asc(arr,low,i)
        quick_sort_asc(arr,i+2,high)

def quick_sort_desc(arr, low, high):
    if low < high:
        # Random Pivot
        pivot_Index = random.randint(low, high)
        pivot_Value = arr[pivot_Index]
        
        swap(arr,pivot_Index,high) #Swap Highest Index Value with the pivot
        i = low -1
        
        for j in range(low,high):
            if arr[j]>pivot_Value:
                i+=1
                swap(arr,i,j)
        
        swap(arr,i+1,high)
        quick_sort_desc(arr,low,i)
        quick_sort_desc(arr,i+2,high)

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Sorted array in ascending:")
    quick_sort_asc(arr, 0, (len(arr)-1))
    for i in range(len(arr)):
        print(f"{arr[i]}", end=" ")
    print()

    print("Sorted array in descending:")
    quick_sort_desc(arr, 0, (len(arr)-1))
    for i in range(len(arr)):
        print(f"{arr[i]}", end=" ")

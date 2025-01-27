from Sorting_Algorithms.bubblesort import *
from Sorting_Algorithms.quicksort import *
from Sorting_Algorithms.insertionsort import *
from Sorting_Algorithms.mergesort import *

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
    print()

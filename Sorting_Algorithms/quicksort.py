import random


def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp


def quick_sort_asc(arr, low, high):
    if low < high:
        # Random Pivot
        pivot_Index = random.randint(low, high)
        pivot_Value = arr[pivot_Index]

        swap(arr, pivot_Index, high)  # Swap Highest Index Value with the pivot
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot_Value:
                i += 1
                swap(arr, i, j)

        swap(arr, i+1, high)
        quick_sort_asc(arr, low, i)
        quick_sort_asc(arr, i+2, high)
    return arr


def quick_sort_desc(arr, low, high):
    if low < high:
        # Random Pivot
        pivot_Index = random.randint(low, high)
        pivot_Value = arr[pivot_Index]

        swap(arr, pivot_Index, high)  # Swap Highest Index Value with the pivot
        i = low - 1

        for j in range(low, high):
            if arr[j] > pivot_Value:
                i += 1
                swap(arr, i, j)

        swap(arr, i+1, high)
        quick_sort_desc(arr, low, i)
        quick_sort_desc(arr, i+2, high)
    return arr
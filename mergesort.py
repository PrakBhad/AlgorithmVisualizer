def merge_asc(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[],
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort_asc(arr, left, right):
    if left < right:
        mid = (right+left)//2
        merge_sort_asc(arr, left, mid)
        merge_sort_asc(arr, mid+1, right)
        merge_asc(arr, left, mid, right)


def merge_desc(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] >= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[],
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort_desc(arr, left, right):
    if left < right:
        mid = (right+left)//2
        merge_sort_desc(arr, left, mid)
        merge_sort_desc(arr, mid+1, right)
        merge_desc(arr, left, mid, right)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Sorted array in ascending:")
    merge_sort_asc(arr, 0, (len(arr)-1))
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    print()

    print("Sorted array in descending:")
    merge_sort_desc(arr, 0, (len(arr)-1))
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

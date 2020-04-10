# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for ii in range(cur_index + 1, len(arr)):
            if arr[ii] < arr[smallest_index]:
                smallest_index = ii

        # TO-DO: swap

        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap_count = 1
    while swap_count >= 1:
        swap_count = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap_count += 1

    return arr


array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
array2 = [76, 44, 3, 12, 60, 71, 100, 34, 22, 38, 99, 74, 45, 3, 67, 2]

print(selection_sort(array))
print(bubble_sort(array))

print(selection_sort(array2))
print(bubble_sort(array2))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr

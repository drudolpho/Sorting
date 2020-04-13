# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    temp = []
    repeat = True
    while len(arrA) > 0 and len(arrB) > 0:

        if arrA[0] < arrB[0]:
            temp.append(arrA[0])
            arrA.pop(0)
        elif arrA[0] > arrB[0]:
            temp.append(arrB[0])
            arrB.pop(0)
        else:
            repeat = False
    temp += arrA + arrB

    return temp


arr3 = [[2], [4], [7], [1], [9], [3], [5], [6]]
arr4 = [2, 4, 7, 1, 9, 3, 5, 6, 11]
arr5 = [1, 2, 3]
arr6 = [1]
arr7 = [99, 67]
arr8 = []


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Make sure it is a list with data
    if not arr:
        return []

    # Base case
    if len(arr) == 1:
        if type(arr[0]) is int:
            return arr
        else:
            return arr[0]

    new_arr = arr

    # Make a list of lists
    if type(arr[0]) is int:
        new_arr = []
        for i in range(0, len(arr)):
            new_arr.append([arr[i]])

    # If there is an odd amount merge to make an even amount
    if len(new_arr) % 2 != 0:
        temp = merge(new_arr[-2], new_arr[-1])
        new_arr.pop(-2)
        new_arr.pop(-1)
        new_arr.append(temp)

    # Merge each pair of lists
    array = []
    for i in range(0, len(new_arr), 2):
        temp = merge(new_arr[i], new_arr[i + 1])
        array.append(temp)
    return merge_sort(array)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr

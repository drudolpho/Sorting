# STRETCH: implement Linear Search				
def linear_search(arr, target):
    # TO-DO: add missing code
    answer = -1
    for i in range(0, len(arr)):
        if arr[i] == target:
            answer = i
        else:
            pass

    return answer  # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    answer = -1
    unanswered = True
    if len(arr) == 0:
        return answer  # array empty

    low = 0
    high = len(arr) - 1

    # TO-DO: add missing code
    while unanswered:
        split = (high - low) // 2
        if target == arr[split]:
            answer = split
            unanswered = False
        elif target < arr[split]:
            high = split
        else:
            low = split + 1

    return answer  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    low = low
    high = high
    middle = (low + high) // 2
    answer = -1

    if len(arr) == 0:
        return answer  # array empty
    # TO-DO: add missing if/else statements, recursive calls

    # Base case
    if arr[middle] == target:
        answer = middle
        return answer

    # Test if target is lower or higher than middle
    if arr[middle] > target:
        high = middle
    else:
        low = middle + 1

    return binary_search_recursive(arr, target, low, high)

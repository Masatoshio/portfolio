#
# Searching through an array

import numpy as np
import timeit


def partition(arr, start, end):

    # set the index to 1 less than the first position of the list
    i = (start - 1)
    # set the pivot point to the last value in the array
    pivot = arr[end]
    # then, for each value in the array
    for j in range(start, end):

        # if the array at that position is less than the pivot point
        if arr[j] <= pivot:
            # increase the index by 1
            i = i + 1
            # switch the position of the current number with the number at
            # index number's position
            arr[i], arr[j] = arr[j], arr[i]

    # switch the end number with the index number + 1
    arr[i+1], arr[end] = arr[end], arr[i+1]

    # return the index number to be used as the partition index
    return i + 1


# quickSort function that sorts the partitioned array
#
# Parameters:
#         arr: the array to partition
#         start: the first position of the array (i.e. 0)
#         end: the last position of the array
#
# Returns:
#        (none)
#
def quickSort(arr, start, end):

    # check that start is less than the end value in case array is null
    if start < end:

        # set p as the partition index taken from the partition function
        p = partition(arr, start, end)

        # quicksort the array before the partition index
        quickSort(arr, start, p - 1)
        # quicksort the array after the partition index
        quickSort(arr, p + 1, end)


# Returns index of x in arr if present, else -1
def binarySearch(arr, l, h, x):

    # Check base case
    if h >= l:

        mid = l + (h - l)/2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, h, x)

    else:
        # Element is not present in the array
        return -1


# create 3 lists using the randint function of sizes 10, 100, and 1000
arr10 = list(np.random.randint(0, 100, 10))
arr100 = list(np.random.randint(0, 1000, 100))
arr1000 = list(np.random.randint(0, 10000, 1000))

x = input("Enter a number to search for: ")

# start timer after user input and before function calls
start = timeit.default_timer()

# sort the array of 10
quickSort(arr10, 0, len(arr10) - 1)

# store the search result in a variable named 'result'
result = binarySearch(arr10, 0, len(arr10)-1, x)

# if the binarySearch function does not return -1
if result != -1:
    # print out that the number is present at which position
    print("The value was found at position", result)
# if result is = 1, then print that the value was not found in the array
else:
    print("Value was not found in array")

# end the timer after function calls
end = timeit.default_timer()

# print out the time results
print("The runtime was: ")
print("{:.6f}s".format(end - start))

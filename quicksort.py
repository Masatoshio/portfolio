
# import timeit to calculate runtime as well as numpy for array generation
import timeit
import numpy as np


# function that performs the partition section of quickSort.
#
# Parameters:
#       arr: the array to partition
#       start: the first position of the array
#       end: the last position of the array
#
# Returns:
#       i + 1: the index number for where the parition is
#
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


# function to implement the binarySearch algorithm
#
# Paramters:
#		arr: the array to search]
#		l: the first number in the array
#		h: the last number in the array
#
# Returns:
#		mid: if number is found
#		-1: if number is not found
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


# create random arrays of sizes 10, 100, and 1000
arr10 = list(np.random.randint(0, 100, 10))
arr100 = list(np.random.randint(0, 1000, 100))
arr1000 = list(np.random.randint(0, 10000, 1000))


# have the user input a number to search for
x = int(input("Enter an integer to search for: "))

# For the array of size 10
# Start timer and run quicksort function and search for x
start1 = timeit.default_timer()
quickSort(arr10, 0, len(arr10) - 1)
end1 = timeit.default_timer()
result = binarySearch(arr10, 0, len(arr10) - 1, x)
# Start a second timer to find the runtime for searching for the first, n/2 (5th), and nth element (10th)
start1a = timeit.default_timer()
binarySearch(arr10, 0, len(arr10) - 1, arr10[0])
binarySearch(arr10, 0, len(arr10) - 1, arr10[4])
binarySearch(arr10, 0, len(arr10) - 1, arr10[9])
end1a = timeit.default_timer()
# print out the time taken to run functions
print("For an array of 10, the runtime was:")
print("{:.8f}s".format(end1 - start1))
print("To find the first, n/2th, and nth values, it took:")
print("{:.8f}s".format(end1a - start1a))
# then print if the user's input was found in the array or not
# if the binarySearch function does not return -1
if result != -1:
    # print out that the number is present at which position
    print("The value was found at position", result)
# if result is = 1, then print that the value was not found in the array
else:
    print("Value was not found in array")


# for the array of size 100
# run the same code but for the array of 100
start2 = timeit.default_timer()
quickSort(arr100, 0, len(arr100) - 1)
end2 = timeit.default_timer()
result = binarySearch(arr100, 0, len(arr100) - 1, x)
# start the second timer for the binary searches and execute them
start2a = timeit.default_timer()
binarySearch(arr100, 0, len(arr100) - 1, arr100[0])
binarySearch(arr100, 0, len(arr100) - 1, arr100[49])
binarySearch(arr100, 0, len(arr100) - 1, arr100[99])
end2a = timeit.default_timer()
# print the results as well as a seperator from the previous lines
print("**************************************")
print("For an array of 100, the runtime was:")
print("{:.8f}s".format(end2 - start2))
print("To find the first, n/2th, and nth values, it took:")
print("{:.8f}s".format(end1a - start1a))
# print the results for the user input
# if the binarySearch function does not return -1
if result != -1:
    # print out that the number is present at which position
    print('The value was found at position', result)
# if result is = 1, then print that the value was not found in the array
else:
    print('Value was not found in array')


# for the array of size 1000
# run the code again for an array of 1000
start3 = timeit.default_timer()
quickSort(arr1000, 0, len(arr1000) - 1)
end3 = timeit.default_timer()
result = binarySearch(arr1000, 0, len(arr1000) - 1, x)
# start timers and binary searches for the arr1000
start3a = timeit.default_timer()
binarySearch(arr1000, 0, len(arr1000) - 1, arr1000[0])
binarySearch(arr1000, 0, len(arr1000) - 1, arr1000[499])
binarySearch(arr1000, 0, len(arr1000) - 1, arr1000[999])
end3a = timeit.default_timer()
# print the results
print("**************************************")
print("For an array of 1000, the runtime was:")
print("{:.8f}s".format(end3 - start3))
print("To find the first, n/2th, and nth values, it took:")
print("{:.8f}s".format(end3a - start3a))
# print results for the user input
# if the binarySearch function does not return -1
if result != -1:
    # print out that the number is present at which position
    print('The value was found at position', result)
# if result is = 1, then print that the value was not found in the array
else:
    print('Value was not found in array')

import os
import timeit
os.system('cls')

# Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
 

def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key 

def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])

# Driver code to test above
arr1 = [64, 34, 25, 12, 22, 11, 90]
arr3 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [64, 34, 25, 12, 22, 11, 90]

print(f'The unsorted array is: {arr1}')

time = timeit.timeit(f"{bubbleSort(arr1)}")
print(f"Sorted Bubble sort array is: {arr1}, and took {time} seconds")

time = timeit.timeit(f"{insertionSort(arr2)}")
print(f"Sorted insertion sort array is: {arr2}, and took {time} seconds")

time = timeit.timeit(f"{selectionSort(arr3, len(arr3))}")
print(f"Sorted selection sort array is: {arr3}, and took {time} seconds")




import os
import time
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
        arr[j+1] = key  #

# Driver code to test above
arr1 = [64, 34, 25, 12, 22, 11, 90]
arr3 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [64, 34, 25, 12, 22, 11, 90]

print(f'The unsorted array is: {arr1}')

bubble_start_time = time.time()
bubbleSort(arr1)
bubble_end_time = "--- %s seconds ---" % (time.time() - bubble_start_time)
print(f"Sorted Bubble sorted array is: {arr1}, and took {bubble_end_time}")


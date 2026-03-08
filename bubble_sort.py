# Bubble Sort algorithm
# Here we swaps the adjacent elements on the basis of there values to set the maximum value at the end of array in each iteration

arr = [1,2,6,3,7,9,5,0,4,10,8]

def bubbleSort(arr):
    n = len(arr)
    while(n > 1):
        # Optimizes the bubble sort by checking if any swap is performed in current loop
        swapped = False
        for i in range(n-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        # If no swap is performed that means array is already sorted
        if not swapped:
            return
        n-=1
    return arr
print(bubbleSort(arr))
# Time Complexity: O(n^2), because of nested loop
# Best Case Time Complexity: O(n), when the array is already sorted, we just need to check once and return
# Space Complexity: O(1)
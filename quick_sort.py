# Quick Sort Algorithm
# Here we create a pivot and partition the array around the pivot, then recursively apply the same logic to the left and right subarrays.
# This is in-place algorithm, meaning it doesn't require additional storage, it does the computations directly inside the array.

def partition(nums, low, high):
    # Taking 1st element as the pivot
    pivot = nums[low]
    i = low
    j = high
    while (i<j):
        while (i<high and nums[i] <= pivot):
            i+=1
        while (j>low and nums[j] >= pivot):
            j-=1
        if(i < j):
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    # return the index of element which is at its correct position
    return j

def quickSort(nums, low, high):
    if(low < high):
        # We get the partition key (index of element which is at its correct position)
        key = partition(nums, low, high)
        # We divide the array into two parts using the partition key
        quickSort(nums, low, key-1)
        quickSort(nums, key+1, high)

# Time Complexity: O(n log n) on average, O(n^2) in the worst case (when the smallest or largest element is always chosen as the pivot, example when all elements are same in the array).
# Space Complexity: O(log n) on average, O(n) in the worst case (when the smallest or largest element is always chosen as the pivot).

array = [10, 7, 8, 9, 1, 5]
n = len(array)
quickSort(array, 0, n-1)
print("Sorted array:", array)
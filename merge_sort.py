# Merge Sort Algorithm
# Here we divide the array into two halves and sort them recursively and then merge the sorted halves
# This is not an in-place algorithm, as it requires additional storage for the temporary arrays used during merging.

def merge_array(left, right):
    sorted_array = []
    i = j = 0
    n, m = len(left), len(right)

    while (i < n and j < m):
        if (left[i] < right[j]):
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    # If there are remaining elements in left or right, add them to the sorted array
    # sorted_array.extend(left[i:])
    # sorted_array.extend(right[j:])
    while (i < n):
        sorted_array.append(left[i])
        i += 1
    while (j < m):
        sorted_array.append(right[j])
        j += 1
    return sorted_array

def merge_sort(arr):
    if (len(arr) <= 1):
        return arr
    # Split the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # Recursively sort the left and right halves and then merge them
    left_half = merge_sort(left)
    right_half = merge_sort(right)
    return merge_array(left_half, right_half)

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)
# Time Complexity: O(n log n) in all cases (best, average, worst)
# Space Complexity: O(n) due to the temporary arrays used for merging
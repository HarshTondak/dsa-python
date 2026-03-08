# Insertion Sort algorithm
# Here we selects the index with minimum value in each iteration to sort the array and set it to the start of the array

arr = [1,2,6,3,7,9,5,0,4,10,8]

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
print(insertionSort(arr))
# Time Complexity: O(n^2), because of nested loop
# Space Complexity: O(1)
# Selection Sort Algorithm
# here we selects the index with minimum value in each iteration to sort the array and set it to the start of the array

arr = [1,2,6,3,7,9,5,0,4,10,8]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIdx = i
        for j in range(i+1, n):
            if(arr[minIdx] > arr[j]):
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr
print(selectionSort(arr))
# Time Complexity: O(n^2), because of nested loop
# Space Complexity: O(1)
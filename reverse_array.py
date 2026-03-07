# We need to reverse an array but only between given indexes
# Lets say given data is: 
# nums = [1,2,3,4,5,6,7,8,9]
# indexes: i=3, j=6 (both included)
# expected output: [1,2,3,7,6,5,4,8,9]

# Python shortcuts that can be used to reverse whole arrays
# 1. nums.reverse()
# 2. nums[::-1]

nums = [1,2,3,4,5,6,7,8,9]
i=3
j=6

# method 1: using loops
def reverse(nums, i, j):
    while(i<j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i+=1
        j-=1
    return nums
print(reverse(nums, i, j))
# Time complexity: O(n/2), in worst case when j-i = size of nums[]
# Space complexity: O(1)

# methods 2: Using recursion
def recReverse(nums, left, right):
    if(left>=right):
        return nums
    nums[left], nums[right] = nums[right], nums[left]
    return recReverse(nums, left+1, right-1)
print(recReverse(nums, i, j))
# Time complexity: O(n/2), in worst case when j-i = size of nums[]
# Space complexity: O(n/2), in worst case because of callstack
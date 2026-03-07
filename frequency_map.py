# Find the frequencies of numbers in a row.
# Using dictionary here

nums = [1,2,3,1,3,5,6,7,1,2,3,3,6,3]
size = len(nums)

# method 1
freq = {}
# Or we can write this => freq = dict()
for i in range(size):
    if (nums[i] in freq):      # Checks if number already exits in dictionary
        freq[nums[i]] += 1
    else:
        freq[nums[i]] = 1
print(freq)
# Time complexity: O(n), since we are iterating all elements of array.
# Time complexity of performing the check for an element in a dictionary in O(1) only
# Space complexity: O(n) since in worst case it can go upto size n.

# method 2
hashmap = {}
for i in range(size):
    hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
print(hashmap)
# Time complexity: O(n), since we are iterating all elements of array.
# Time complexity of performing the check for an element in a dictionary in O(1) only, here we are using the get() of dictionary for this purpose.
# Space complexity: O(n) since in worst case it can go upto size n.
# Hashing is basically pre-storing the hash values of the keys in a dictionary, so that we can quickly look up the value associated with a key without having to compute the hash value every time.

# Find the number of occurences of each element of m[] inside the n[].
# m = [7,3,4,1,8,6,5]
# n = [10,1,2,3,4,5,7,3,3,4,1,0,8,0,8,8,6,5,3]

m = [7,3,4,1,8,6,5,9]
n = [1,2,3,4,5,7,3,3,4,1,0,8,0,8,8,6,5,3,10]
# method 1: we traverse each element of m[] and check it's occurence inside n[] one by one
# Time complexity: O(n x m), because of nested looping.
# Space complexity: O(k), because we will be using some variables only.

# method 2: Using Hashing
# First create a hashmap of n[]
hashMap = {}
size = len(n)
for i in n:
    hashMap[i] = hashMap.get(i, 0) + 1
# Check occurence of elements of m[] using hashmap
for i in m:
    if(hashMap.get(i, 0) != 0):
        print(i, "occurs", hashMap[i], "times")
    else:
        print(i, "not found!")
# Time complexity: O(n + m), almost equals to O(n).
# Time complexity of performing the check for an element in a dictionary in O(1) only
# Space complexity: O(n) since in worst case it can go upto size n.

# hashing can be performed on string elements as well
# x = ["a", "a", "b", "c"]
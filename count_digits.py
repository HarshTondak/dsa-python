# sample number
num = 12345678

# method 1: using mathematical operations
count = 0
temp_num = num
while temp_num > 0:
    temp_num = temp_num // 10       # remove the last digit
    count += 1
print("Number of digits in", num, "is:", count) # Output: 8
# Time complexity: O(d), where d is the number of digits in the number
# or we can say O(log10(n)), where n is the number itself, since the number of digits grows logarithmically with the value of the number.
# Space complexity: O(1) since we are using a constant amount of space to store the count and temporary variable.

# method 2: using logarithmic properties
from math import *
if num > 0:
    count_log = floor(log10(num)) + 1
print("Number of digits in", num, "is:", count_log) # Output: 8
# Time complexity: O(1) since we are using a constant-time logarithmic operation.
# Space complexity: O(1) since we are using a constant amount of space to store the count.

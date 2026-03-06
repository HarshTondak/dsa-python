# sample number
num = 123454321

# method 1: using mathematical operations
temp_num = num
reversed_num = 0
while temp_num > 0:
    digit = temp_num % 10
    reversed_num = reversed_num * 10 + digit
    temp_num = temp_num // 10

if num == reversed_num:
    print(num, "is a palindrome number.")
else:
    print(num, "is not a palindrome number.")

# Time complexity: O(d), where d is the number of digits in the number, since we need to iterate through each digit to reverse it.
# Space complexity: O(1) since we are using a constant amount of space to store the reversed number and temporary variable.
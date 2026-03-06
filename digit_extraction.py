# sample number
num = 12345

# extracting using mathematical operations
digits = []
temp_num = num
while temp_num > 0:
    digit = temp_num % 10   # get the last digit
    digits.append(digit)    # add it to the list
    temp_num //= 10         # remove the last digit
print(digits)               # Output: [5, 4, 3, 2, 1]

# Time complexity: O(d), where d is the number of digits in the number, since we need to iterate through each digit.
# Space complexity: O(d) since we are storing all the digits in a list.

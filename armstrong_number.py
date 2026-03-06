# sample number
num = 153       # 1^3 + 5^3 + 3^3 = 153

# method 1: using mathematical operations
def armstrong(num):
    temp_num = num
    total = 0
    while temp_num > 0:
        digit = temp_num % 10
        total += digit ** 3
        temp_num = temp_num // 10
    return total

sum = armstrong(num)
if sum == num:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")

# Time complexity: O(d), where d is the number of digits in the number, since we need to iterate through each digit to reverse it.
# Space complexity: O(1) since we are using a constant amount of space to store the reversed number and temporary variable.
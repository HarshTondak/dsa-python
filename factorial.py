# Find the factorial of a number
# 5! = 5x4x3x2x1

# method 1: Using loops
def factorial(num):
    fact = 1
    for i in range(2, num+1):
        fact = fact*i
    return fact
print(factorial(5))
# Time complexity: O(n)
# Space complexity: O(1)

# method 2: Using Recursion
def recFact(num):
    if(num == 1):
        return 1
    fact = recFact(num-1)
    return fact*num
print(recFact(5))  
# Time complexity: O(n)
# Space complexity: O(n), because we are filling callstack also
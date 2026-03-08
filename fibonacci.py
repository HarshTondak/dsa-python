# Fibonacci series
# Check if the given number is a part of fibonacci series or not
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377

# method 1: using mathematical operations
def fibonacci(num):
    a=0
    b=1
    while(a <= num):
        if(a + b == num):
            return True
        a, b = b, a+b
    return False
print(fibonacci(377))
# Time complexity: O(log(n)), because we are incrementing very fast
# Space complexity: O(1)

# method 2: using recursion
def recFibonacci(num, a, b):
    if(a+b == num):
        return True
    elif(a+b > num):
        return False
    a, b = b, a+b
    return recFibonacci(num, a, b)
print(recFibonacci(376, 0, 1))
# Time complexity: O(log(n)), because we are incrementing very fast
# Space complexity: O(log(n)), because of callstack usage


# Find the nth value in the fibonacci series
# There is a concept of fib(n) = fib(n-1) + fib(n-2)

# method 1: using mathematical operations
def getfibonacci(num):
    if(num == 0 or num == 1):
        return num
    a=0             # Zero Index
    b=1             # 1st Index
    while(num > 1):
        a, b = b, a+b
        num-=1
    return b
print(getfibonacci(15))
# Time complexity: O(n)
# Space complexity: O(1)

# method 2: using recursion
def getrecfibonacci(num):
    if(num == 0 or num == 1):
        return num
    return getrecfibonacci(num-1) + getrecfibonacci(num-2)
print(getrecfibonacci(7))
# Time complexity: O(2^n), because of two recursion trees
# Space complexity: O(2^n)
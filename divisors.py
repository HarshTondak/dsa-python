# 10 = [1, 2, 5, 10]

# method 1: brute force
def getDivisors(num):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result
print(getDivisors(100))
# Time complexity: O(n), since we are iterating all numbers from 1 to num+1.
# Space complexity: O(k) since we are using a constant amount of space to store the divisors.

# method 2: optimized version
def getDivisors2(num):
    result = []
    for i in range(1, num//2 + 1):
        if(num % i == 0):
            result.append(i)
    result.append(num)
    return result
print(getDivisors2(100))
# Time complexity: O(n/2), since we are iterating all numbers from 1 to num+1.
# Space complexity: O(k) since we are using a constant amount of space to store the divisors.

# method 3: most optimized version (square root method)
def getDivisors3(num):          # lets say num=36
    result=[]
    for i in range(1, int(num ** 0.5) + 1):     # range(1,7)
        if(num % i == 0):
            result.append(i)                    # 1, 2, 3, 4, 6
            if(num//i != i):
                result.append(num//i)           # 36, 18, 12, 9
    return result
print(getDivisors3(36))
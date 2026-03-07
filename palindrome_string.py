# Palindrome check for strings
# Example: nitin, mom etc...

name = "nitin"

# method 1: using loops
def isPalindrome(str):
    i,j = 0,len(str)-1
    while(i<j):
        if(str[i] == str[j]):
            i+=1
            j-=1
        else:
            return False
    return True
print(isPalindrome(name))
# Time complexity: O(n/2)
# Space complexity: O(1)

# method 2: using recursion
def recPalindrome(str, left, right):
    if(left >= right):
        return True
    if(str[left] != str[right]):
        return False
    return recPalindrome(str, left+1, right-1)
print(recPalindrome(name, 0, len(name)-1))
# Time complexity: O(n/2)
# Space complexity: O(n/2), because of callstack
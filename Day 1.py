# Python Program to Check if a String is Palindrome or Not

def check_palindrome(s):
    return s == s[::-1]


if check_palindrome("malayalam"):
    print('Yes')
else:
    print('No')
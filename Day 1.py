# Python Program to Check if a String is Palindrome or Not

def check_palindrome(s):
    return s == s[::-1]


if check_palindrome("malayalam"):
    print('Yes')
else:
    print('No')

#List Slicing

Lst = [50, 70, 30, 20, 90, 10, 40]
print(Lst[::3])

List = ['Geeks', 4, 'geeks !']
print(List[::-2])

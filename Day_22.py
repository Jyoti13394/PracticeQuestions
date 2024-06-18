# Palindrome of a string

string_palin = "malayalam"

def check_if_palindrome(strng):
    return strng[::] == strng[::-1]


print(check_if_palindrome(string_palin))

# Python | Swap commas and dots in a String

Input_string= "14, 625, 498.002"
#Expected_Output= "14.625.498.002"

def string_replication(input_string):
    return input_string.replace(', ')

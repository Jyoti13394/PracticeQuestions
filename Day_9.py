# Write a Python program to sum recursion lists.

def sum(input_list):
    total = 0
    for element in input_list:
        if type(element) == type([]):
            total = total + sum(element)
        else:
            total = total + element
    return total

print(sum([[2,4,5],1, 2, [3,4],[5,6]]))


# Write a Python program to get the factorial of a non-negative integer.

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * (fact(n-1))


print(fact(5))


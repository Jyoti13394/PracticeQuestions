# To return 1 if all elements in list are palindrome else 0

def PalinArray(arr, n):
    list_1 = []
    for each in arr:
        print(str(each)[::-1])
        if str(each) == str(each)[::-1]:
            list_1.append(1)
        else:
            list_1.append(0)

    if 0 not in list_1:
        print(1)
    else:
        print(0)


# Print pattern-
# For N = 2 the pattern will be
# 2 2 1 1
# 2 1

def PatternPrinting(n):
    if n == 1:
        print(n)
    elif n == 0:
        print()
    else:
        for j in range(n, 0, -1):
            for i in range(n, 0, -1):
                print(str(i) * j, end = '$')



PatternPrinting(2)

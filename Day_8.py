# Find the missing number in the array

list_1 = [2, 4, 3, 1, 5, 8, 7]
n = 8


def missing_number(list_1):
    length_of_array = len(list_1)
    missing_num = (n * (n + 1) / 2) - sum(list_1)
    return int(missing_num)


print(missing_number(list_1))

# Pythagorean Triplet in an array
# Write a function that returns True if there is a Pythagorean triplet that satisfies a2+ b2 = c2

s = [3, 1, 4, 6, 5]  # True


# s = [10, 4, 6, 12, 5] #False

def check_triplet(s):
    s= sorted(s)
    for i in s:
        #print(i)
        for j in s:
            #print(j)
            for k in s:
                if i*i + j*j == k*k:
                    return True
    else:
        return False


print(check_triplet(s))

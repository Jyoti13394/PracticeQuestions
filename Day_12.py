from collections import Counter
# Sort a list without using a sort keyword

lis1 = [67, 68, 54, 89, 2, 4, 80, 65, 33, 44, 23, 67]

sorted_list = []

for i in range(0, len(lis1)):
    for j in range(i + 1, len(lis1)):
        if lis1[i] > lis1[j]:
            lis1[i], lis1[j] = lis1[j], lis1[i]

print(lis1)


# Python program to find out common letter in 2 strings

string_1 = 'NAINA'
string_2 = 'REENE'

common_letters = []
for each_word in string_1:
    if each_word in string_2:
        common_letters.append(each_word)

print(set(common_letters))

# Write a program to count the frequency of words appearing in string
string_3 = 'Sheena loves eating apple and mango. Her sister also loves eating apple and mango'
list_1 = string_3.split()
print(Counter(list_1))




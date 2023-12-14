from collections import Counter

def find_common_string(string_1, string_2):
    return set(string_1) & set(string_2)


print(find_common_string(string_1='Jyoti Prasad', string_2='Hrithik Kumar'))


# Count of frequency of words appearing in string

string_11 = "In this Selenium Python Tutorial, we will learn how to find element by ID or Name."

list_1 = string_11.split()
print(Counter(list_1))

# Write a program to convert 2 list into a dictionary

list1 = ['Naina', 'Kimi', 'Sheena']
list2 = [876878, 9809]
print(list1[-1])



def conv_list_to_dict(list1, list2):
    d = {}
    # if len(list1) != len(list2):
    #     print("Please make sure the lists have equal number of elements")
    # else:
    try:
        for i in range(len(list1)):
            d[list1[i]] = list2[i]
        print(d)
    except Exception as e:
        print(e)

conv_list_to_dict(list1, list2)

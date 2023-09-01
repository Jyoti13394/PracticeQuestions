# Q.1) Python | Ways to remove a key from dictionary

test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}

#print(test_dict.items())
#Concet of items() method
for key, val in test_dict.items():
    print(key, val)
new_dict = {key: val for key, val in test_dict.items() if key != 'Mani'}
print(new_dict)

# Using del
del test_dict['Mani']
print(test_dict)

# Q.2) Python – Extract Unique values dictionary values

test_dict_1 = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}

print(test_dict_1.values())
''''
uniq_values = set()
for values in test_dict_1.values():
    for ele in values:
        uniq_values.add(ele)
print(list(uniq_values))
'''
# Using list comprehension

uniq_values = list({ele for values in test_dict_1.values() for ele in values})
print(uniq_values)


# Q.3) Ways to sort list of dictionaries by values in Python – Using lambda function
# Ways to sort data in python (By using lambda function or by using itemgetter)
# using sorted and lambda to print list sorted
# by both age and name
list_of_dict = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

print(sorted(list_of_dict, key= lambda i : (i['age'], i['name']), reverse=True))

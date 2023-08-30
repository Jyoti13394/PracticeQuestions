# Remove multiple elements from a list in Python

def remove_element(list_1, remove_elements):
    new_list = [element for element in list_1 if element not in remove_elements]
    return new_list


print(remove_element([11, 5, 17, 18, 23, 50, 5], {11, 5}))

# Python program to find Cumulative sum of a list
Input : list = [10, 20, 30, 40, 50]
#Output : [10, 30, 60, 100, 150]
print(Input[0:0:1])

def cummulative(input_list):
    '''
    cum_list = []
    j = 0
    for i in range(0, len(input_list)):
        j += input_list[i]
        cum_list.append(j)
    '''
    cum_list = [sum(input_list[0:elem:1]) for elem in range(0, len(input_list))]
    return cum_list[1:]


print(cummulative([10, 20, 30, 40, 50]))

#Python | Count occurrences of an element in a list

def count_value(list_of_num, x):
    count_of_x = 0
    for element in list_of_num:
        if element == x:
            count_of_x += 1
    return count_of_x


print(count_value([15, 6, 7, 10, 12, 20, 10, 28, 10], 10))


#Break a list into chunks of size N in Python

def divide_chunks(list_1, n):
    new_list = []
    x = 0
    for i in range(x, x + n):
        new_list.append(list_1[x: x + n])
        x = x + n
        if x > len(list_1):
            break
    return new_list


print(divide_chunks(['geeks', 'for', 'geeks', 'like','geeky','nerdy', 'geek',
                                                          'love','questions','words', 'life'], 4))



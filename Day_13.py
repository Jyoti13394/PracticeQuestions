Input_string= "ABACF"


empty_list = []


def longest_substring(Input_string):
    for i in Input_string:
        while i not in empty_list:
            #print(i)
            empty_list.append(i)

    new_string = "".join(element for element in empty_list)

    return new_string


print(longest_substring(Input_string))

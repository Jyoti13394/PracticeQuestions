Input = [12, 35, 9, 56, 24]
#Output : [24, 35, 9, 56, 12]


def interchange(lst):
    if len(lst) < 2:
        print("Minimum length of list should be 2")
    else:
        lst[0], lst[-1] = lst[0], lst[-1]
        print(lst)

interchange(Input)

# Python Program to Swap Two Elements in a List

Input_List = [3, 5, 1, 9]
pos1 = 1
pos2 = 3
# Output : [19, 65, 23, 90]

def swap_list_elements(lst, pos_1, pos_2):
    Input_List[pos_1] = Input_List[pos_1] + Input_List[pos_2]
    Input_List[pos_2] = Input_List[pos_1] - Input_List[pos_2]
    Input_List[pos_1] = Input_List[pos_1] - Input_List[pos_2]
    return Input_List

print(swap_list_elements(Input_List, pos1, pos2))

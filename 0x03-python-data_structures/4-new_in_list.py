#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list:
        list_1 = my_list.copy()
        if idx < 0 or idx >= len(list_1):
            return list_1
        else:
            list_1[idx] = element
            return list_1

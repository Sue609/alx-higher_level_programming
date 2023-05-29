#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            result = 0
            if i < len(my_list_1) and i < len(my_list_2):
                if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                    result = my_list_1[i] / my_list_2[i]

                else:
                    print("wrong type")
            elif i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")

        except ZeroDivisionError:
            print("division by 0")

        finally:
            new_list.append(result)

    return new_list

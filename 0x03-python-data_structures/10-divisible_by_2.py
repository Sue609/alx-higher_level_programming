#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    
    result = []

    for divisor in my_list:

        if divisor % 2 == 0:
            result.append(True)

        else:
            result.append(False)
    return result
            

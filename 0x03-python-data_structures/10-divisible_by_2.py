#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    num = []
    for i in my_list:
        if i % 2 == 0:
            num.append(True)
        else:
            num.append(False)
    return num

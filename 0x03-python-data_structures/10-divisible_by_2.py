#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    muls = []
    for i in my_list:
        if i % 2 == 0:
            muls.append(True)
        else:
            muls.append(False)
        return (muls)

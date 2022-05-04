#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = sum(a * b for a, b in my_list)
    weight = sum(b for a, b in my_list)
    return score/weight

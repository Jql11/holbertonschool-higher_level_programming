#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    only_1 = [i for i in set_1 if i not in set_2]
    only_2 = [i for i in set_2 if i not in set_1]
    return only_1 + only_2

#!/usr/bin/python3
def weight_average(my_list=[]):
    score = sum([x[1] * x[0] for x in my_list])
    weight = (sum([x[1] for x in my_list]) or 1)
    return (score / weight)

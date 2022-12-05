#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = []
    for i in range(0, len(tuple_a)):
        tuple_sum.append(tuple_a[i] + tuple_b[i])
    tuple_sum = tuple(tuple_sum)
    print(tuple_sum)

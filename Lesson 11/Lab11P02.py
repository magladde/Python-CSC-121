# Lab 11 problem 2
import random


def main():
    set1 = get_random()
    print('set1:', set1)

    set2 = get_random()
    print('set2:', set2)

    union1 = get_union(set1, set2)
    print('Union of set1 and set2:', union1)

    odd_set = find_odd(union1)
    print('Odd numbers in union of set1 and set2:', odd_set)

    intersected_set = find_intersection(set1, set2)
    print('Intersection of set1 and set2:', intersected_set)

    symmetric_difference = find_difference(set1, set2)
    print('Symmetric difference of set1 and set2:', symmetric_difference)

def get_random():
    set1 = {random.randint(1,10) for x in range(5)}
    return set1

def get_union(x, y):
    union1 = (x | y)
    return union1

def find_odd(y):
    odd_set = {x for x in y if x % 2 == 1}
    return odd_set

def find_intersection(x, y):
    intersected_set = (x & y)
    return intersected_set

def find_difference(x,y):
    symmetric_difference = (x ^ y)
    return symmetric_difference

main()
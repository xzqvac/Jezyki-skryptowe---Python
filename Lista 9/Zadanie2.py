"""Measure data"""
import numpy as np
import sys

#print("Jestem: ", __name__)


def str_to_list(args):
    return [int(i) for i in args]


def average(args):
    avg = np.average(args)
    return avg


def variance(args):
    var = np.var(args)
    return var


def deviation(args):
    dev = np.std(args)
    return dev


if __name__ == '__main__':

    if len(sys.argv) < 2:
        list1 = []
        for line in sys.stdin:
            list1.append(int(line))
    else:
        list1 = str_to_list(sys.argv[1:])
    print("Średnia: ", average(list1))
    print("Wariancja: ", variance(list1))
    print("Odchylenie standardowe: ", deviation(list1))


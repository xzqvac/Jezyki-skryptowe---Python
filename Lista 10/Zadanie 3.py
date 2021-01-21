import itertools
import random

class sublists:
    def __init__(self,number):
        self.number = number
    def lists(self):
        lista = [random.randint(-10,10) for i in range(self.number)]

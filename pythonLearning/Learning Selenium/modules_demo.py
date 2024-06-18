# https://docs.python.org/3/library/

import math
from math import sqrt
import inheritance as file

class Modules_demo():
    def built_in_modules(self):
        print(math.sqrt(100))
        print(sqrt(500))

    def car_description(self):
        make = "BMW"
        file.Car.drive(make)


a = Modules_demo()
a.built_in_modules()
a.car_description()

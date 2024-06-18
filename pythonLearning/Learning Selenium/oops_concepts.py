var = "This is a string"
print(type(var))
var.upper()


class Car():

    wheels = 4     # member variable

    def __init__(self, model, make):
        self.model = model
        self.make = make
        print("the car is honda")

    def info(self):
        print("model of the car is " + self.model)
        print("make of the car is " + self.make)


a = Car("amaze", "Honda")
a.info()

b = Car("E250", "Benz")
b.info()
print(Car.wheels)

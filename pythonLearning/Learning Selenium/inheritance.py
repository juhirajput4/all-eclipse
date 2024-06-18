class Car():

    def __init__(self, make):
        self.make = make
        print("car instance created")

    def drive(self):
        print("car starts")
        print("mke of the car is " + self.make)

    def stop(self):
        print("car stops")


class Honda(Car):

    def __init__(self):
        Car.__init__(self, "suzuki")
        print("honda instance create")

    def drive(self):
        super(Honda,self).drive()
        super(Honda, self).stop()
        print("honda drives very fast")

# a = Car("amaze")
# a.drive()
# a.stop()

b = Honda()
b.drive()
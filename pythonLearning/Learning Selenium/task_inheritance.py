class Fruit():
    def __init__(self, model):
        self.model = model
        print("there are many fruits")
    def nutrition(self):
        print("It gives us nutrition " + self.model)
    def fruit_shape(self):
        print("there are many shapes of the fruits")

class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self,"like vitamin")
        print("I love orange")

    def nutrition(self):
        super(Apple, self).nutrition()
        print("I love apple")

    def color(self):
        print("red color")

a = Apple()
a.nutrition()
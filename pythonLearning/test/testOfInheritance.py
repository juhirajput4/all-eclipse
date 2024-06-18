class Animal():
    def __init__(self, name):
        self.name = name
        print("constructoor of the parent")
    def print_name(self):
        print("name of the animal is " + self.name)

class Cat(Animal):
    def __init__(self,name):
        self.name = name

    def makeSound(self):
        print('Mew Mew')

    def makeSound(self, num):
        print('Mew Mew ' + str(num))
        
    def print_name(self):
        super(Cat, self).print_name()
        print("name of the cat animal is " + self.name)

c = Cat('cat')
c.print_name()
c.makeSound(4)
c.makeSound()
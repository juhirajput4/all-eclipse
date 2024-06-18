class Animal():
    def __init__(self,name,sound,food,age=0):
        self.name = name
        self.sound = sound
        self.food = food
        self.age = age
    def displayProp(self):
        print("name of the animal is " + self.name)
        print("sound of the animal is " + self.sound)
        print("animal eats " + self.food)
    def addAge(self,num):
        self.age = self.age + num

    def getAge(self):
        return self.age

cat = Animal("cat","meaw", "milk",4)
cat.displayProp()
print('age before',cat.getAge())
cat.addAge(2)
print(cat.getAge())

dog = Animal("dog","bark","milk")
dog.displayProp()

"""
def displayProp(sound, food):
    print("sound of the cat is " + sound)
    print("cat eats " + food)

displayProp("meaw", "milk")"""




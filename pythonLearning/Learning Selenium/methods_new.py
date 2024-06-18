"""
A group of code statements which can perform some specific task is method
Methods are reusable and can be called when needed in the code
"""
def sum():
    print(2 + 3)   # These are static parameters
sum()

def add(a = 6, b = 8):
    """
    this code is adding two numbers
    a, b these are the integers
    """
    c = a+b
    return c
x = add()
print(x)
add(2,2)
z = add("one",str(5))
print(z)





# second program
def isMetro(city):
    l = ["delhi","mumbai","gzb"]
    if city in l:
        return True
    else:
        return False
c = isMetro("noida")
print(c)


#Variable scope

s = 10

def test():
    global s
    print("value of local 's' is" + str(s))
    s = 3
    print("new value of local s is " + str(s))

print("value of global s is " + str(s))
test()
print("did the value of global s change? " + str(s))
print(s + 10)



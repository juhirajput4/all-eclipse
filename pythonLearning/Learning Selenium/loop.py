"""
While Loop
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""
x = 0
while x <= 5:
    print("value of x is " + str(x))

    x = x+1

l = []
num = 0
while num < 10:
    num = num+1
    l.append(num)
    print("the value of num is " + str(num))
print(l)


"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""
"""print("*" * 20)
l = []
num = 0
while num < 10:
    num = num+1
    l.append(num)
    while num == 5:

        print("the second loop is on")
        continue
    print("the value of num is " + str(num))
print(l)"""

"""
For Loop
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""

nums = [1, 2, 3, 4]
for num in nums:
    print(num * 20)

str = "abcabc"
for s in str:
    # print(s, end=" ")
    if s == "a":
        print("A", end="+")
        # print("A")
    else:
        print(s, end="-")
print(" ")

d = {"k1" : "one", "k2" : "two", "k3" : "three"}
for dic in d:
    #print(d[dic])
    print(dic + " " + d[dic])

# iterating multiple list using zip function
var = [23, 3, 4, 5, 90, 30, 40]
var2 = [7, 8, 6, 9, 100, 81]
for a, b in zip(var, var2):
    if a > b:
        print(a)
    else:
        print(b)
    # print(a)
    # print(b)


print(list(range(10)))

for v in range(10,100):
    print(v)












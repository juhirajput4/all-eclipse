"""
Exceptions are errors
We should handle exceptions in our code
to make sure the code is working the way we want and is handling all the unwanted issues
Link to 3.5 built-in exceptions - https://docs.python.org/3/library/exceptions.html
"""

def exception_handling():
    try:
        a = 10
        b = 30
        c = 10
        d = (a + b)/c
        print(d)

    except ZeroDivisionError:
        print("in the except block")
    except TypeError:
        print("cannot add string")
        
    else:
        print("as there was no exception, else block is executed")


exception_handling()


"""
Create a dictionary "car"
 Create 3 keys
 1. make
 2. model
 3. year
 Try to access the color key. Remember, we never created the color key, so it's
 going to throw an exception. You need to handle the exception using the try,
 except and finally block.
"""
def dictionary():
    try:
        dic = {"make":"Car", "model":"A2010", "year":"2022"}
        # print("here we want to get the values of the dicionary is " + str(dic.values()))
        # print("here we want to get the items of the dicionary is " + str(dic.items()))
        # print("here we want to get the values of the make is " + str(dic["make"]))
        print("here we want to get the values of the color is " + str(dic["color"]))

    except KeyError:
        print("error")

    else:
        print("as there was no exception, else block is executed")


dictionary()

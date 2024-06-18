"""m=0
while m<=5:
    m=m+1
    print(m)
    while m==5:
        print('in 5 loop')
        break
    print('prateek')
print('out of loop')"""

# Sum of 1 to 100
m = 1
sum=0
while m <= 10:
    sum = sum + m
    m=m+1
print(sum)

# Multiple parameter in a method
def add_multi_para(a,b, *arg, **kwarg):
    sum = a + b
    print('C',arg)
    for i in arg:
        sum = sum + i
    print('kwarg',kwarg)
    for key , value in kwarg.items():
        sum = sum + value
    print(sum)

add_multi_para(4,4)

add_multi_para(4,6,5,4,e=10,f=20)

# Print words of sentence
def fun(*args):
    for i in args:
        print(i, end=" ")

    print(" ")
    print(len(args))

fun('My','name','is', 'juhi','rajput')

fun('My', 'name', 'is', 'Prateek')











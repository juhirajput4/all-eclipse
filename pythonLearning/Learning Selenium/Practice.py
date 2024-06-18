var = [213, 452, "juhi"]
print(type(var))
print(var)
print(var[1])

p = [1, 2, 3, [23, 45]]
print(p[3][0])

q = [41, 23, 71, [78, 56, "shubhi"], 400]
print(q[4])
print(q[3][2])
q[3][1]= 100
print(q)

# s = [23, 45, 100, 34, 98]
# s.sort()
# print(s)
# s.sort(reverse=True)
# print(s)


# tuple is a immutable
tuple = (34, 46, 100, "juhi", "chhavi", 46)
print(type(tuple))
t = len(tuple)

print(t)

#boolean

z = True
print(type(z))

#dictionary

dic = {"a": "chhavi", "b": "shubhi", "c": [123, 456]}
print(type(dic))
print(dic.items())
print(dic.keys())
print(dic.values())
print(dic["b"])
print(dic["c"][0])

#sets
sets = {123, 45, 100}
print(type(sets))
print(sets)

a, b,  c, d = 10, 40, 20, 30

print(b)

m = "am"
n= "language"
print("I " + m +" loving python " + n)
print("I %s loving python %s " % (m,n))





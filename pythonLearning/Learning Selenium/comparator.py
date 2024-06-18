"""
 ==  value equality
 !=  not equal to
 <   less than
 >   greater than
 <=  less than or equal
 >=  greater than or equal to
  10>= 9
"""

var = 10 == 10
print(var)
print(type(var))

""" 
 and  (It is case sensitive)
 true and true = true
 true and false = false
 false and false = false
 
 or (It is case sensitive)
 true or true = true
 true or false = true
 false or false = false
 
 not
 not true = false
 not false= true
 
"""
a = (10 != 10) and (7 < 5)
print(a)

b = (10 > 10) or (6>6)
print(b)

print(not(b))

c = not(5 >= 1)
print(c)




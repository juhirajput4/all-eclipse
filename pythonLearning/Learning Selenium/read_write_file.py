"""
Manual steps to write to a file
1. open notepad and create a file
2. write in the file
3. close the file

mode -
1. read mode: r
2. write mode: w
3. append mode: a
4. read/write mode: r+
"""
#file = open("D:/python selenium/new_file.txt", "w")
file = open("abc.txt", "w")
file.write("my personal file")
file.close()


f = open("D:/python selenium/new_file2.txt", "w")
list = [3,45,67,89,10]
for i in list:
    f.write(str(i) + "\n")
f.close()

s = open("D:/python selenium/new_file2.txt", "r")
#print(s.read())
print(s.readline())
s.close



# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
###delaring variables
class_number = 5300
print "class number is: ", class_number
class_name = "practical genomics"
print "class name is: ", class_name
students = ["Tom", "Sarah", "Anne", "Bob"] #list of strings
print "students in the class are: ", students
len(students)
grades=[86, 90,84, 95]
len(grades)
info=(["Masters",1], "phD", ["Masters"], 3)

###accessing elements in a tuple or list
info[0]
info[0][1]
info[3]
info[2]
info[2][1]
students[0]
students[-1]
students[-2]
students[-5]
students[2::1]
students[::-1]
students[:2:2]
students[:3:2]
students[0::2]
students.index("Bob")
students[3]="Tyler"
students[3]
students.append("Bob")
students.index("Bob")
students[2]="Alex"


###for and while loops
for s in students:
    print s
    
index=0

while index<len(students):
    print index
    print students[index]
    index=index+1
    
numbers=range(10)
print numbers
numbers=range(1,11,1)
print numbers
range(2,11,2)

###using the range function to print numbers from 1 through 9   
for a in range (1,10):
    print a
    
###playing with strings    
s = students[2]
print s
s[0]
s[0]+s[1]
len(s)

###constructing if statements
apples = 5
oranges = 10

if apples == oranges:
    print "equal"
else:
    print "not equal"
    

if apples == oranges:
    print "equal"
elif apples > oranges:
    print "more apples"
elif apples < oranges:
    print "less apples"
else:
    print "not equal"
    
if apples == oranges:
    print "equal"
elif apples < oranges:
    print "less apples"
    apples=10
    print apples
elif apples > oranges:
    print "more apples"
else:
    print "not equal"
    

###indentation MATTERS!    
for s in students:
    print s

for s in students:

print s 
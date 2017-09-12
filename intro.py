###declaring variables
class_number = 5300
print "class number is: ", class_number
class_name = "practical genomics"
print "class name is: ", class_name
students = ["Tom", "Sarah", "Anne", "Bob"] #list of strings
print "students in the class are: ", students
grades = [86, 90, 84, 95] #list of integers
print "student grades are: ", grades
info = (["Masters", 1], "phD", ["phD"], "Masters") #tuple
print info

###playing with lists
print students[0]
print students[-1]
print students[-2]
print students[-5]
print students[::1]
print students[::-1]
print students[3:0:-1]
print students[3::-1]

index = 0
while index < len(students):
  print index
  print students[index]
  index = index + 1
  
for s in students:
  print s

a=range(10)
a=range(1,10+1)
a=range(2,10+1,2)

###playing with strings
student = "Sarah"
print student
print len(student)
print student[0]
print student[0]+student[1]+student[2]+student[3]+student[4]

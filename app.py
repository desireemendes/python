#get info from file, r+ to read and write
# employee_file = open("employee.txt", "r")
# for employee in employee_file.readlines():
#   print(employee)
# employee_file.close()

# "a" to append to file, add text onto it
# employee_file = open("employee.txt", "a")
# employee_file.write("\nToby - Human Resources")

#import from student file class student
from Student import Student

student1 = Student("Jason", "Business", 3.1, False)
print(student1.name)
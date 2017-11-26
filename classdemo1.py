#This code explains the concepts of classes in python
# !/usr/bin/python

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

#adding attributes
emp1.age=7

#accessing class attributes function
hasattr(emp1,'age')
setattr(emp1,'age',8)

#built in class attributes

print "Employee.__doc__:",Employee.__doc__
print "Employee.__name__:",Employee.__name__


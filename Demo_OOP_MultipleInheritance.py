# Demo Program in python for multiple inheritance

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printName(self):
        print(self.firstname, self.lastname)

class Employee:
    def __init__(self,empid,salary):
        self.empid=empid
        self.salary=salary

    def printSalary(self):
        print("Emp ID:",self.empid)
        print("Salary:",self.salary)

class Manager(Person,Employee):
    def __init__(self,fname,lname,empid,salary,dept):
        Person.__init__(self,fname,lname)
        Employee.__init__(self,empid,salary)
        self.department=dept

    def printDept(self):
        print("Department:",self.department)


mgr1=Manager("Ashish", "Patil","E-004",100000,"HR")
mgr1.printName()
mgr1.printSalary()
mgr1.printDept()

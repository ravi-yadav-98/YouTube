'''
Classmethod in Python: @classmethod: part:01

-> A class method is bound to the class and not the object of the class.
-> It can access only class variables.
-> It can modify the class state.
-> The class method has a cls as the first parameter


Usecases:

part:01
- Modify Class Attributes/manage class level attributes
- Alternative constructor


part:02
- factory method
- Singleton Design Pattern
- Classmethods in inheritance



Instance method: Bound to a object state
'''
from datetime import date


class Employee:

    CompanyName = 'ABC Interprise'  #class attribute

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


    @classmethod
    def create_Employee_with_fullname(cls, fullname, age):
        firstname, lastName = fullname.split()   # Riya Verma ['Riya','Verma']
        return cls(firstname, lastName, age)

    @classmethod
    def create_Employee_with_DOB(cls, firstname, lastname, DOB):  #12-01-1994
        DOY         = int(DOB.split('-')[-1])
        currentyear = date.today().year  #2023
        age  = currentyear - DOY 
        return cls(firstname, lastname, age)


    
    def get_details(self):   #instace method
        print("Employee Details:")
        print("Employee Full Name: ", self.firstname+' '+self.lastname)
        print("Employee Age: ", self.age)
    
    @classmethod
    def get_company_name(cls):   #class method
        print("Company name: ", cls.CompanyName)


emp = Employee("Amit", 'Shukla', 27)
# emp.get_company_name()
# print(emp.CompanyName)   #class level attribute
# Employee.get_company_name()   #classmethod
# emp.CompanyName = 'Google'
# print(emp.CompanyName)
# emp.get_company_name()

# Employee.CompanyName = 'ABC limited'
# emp.get_company_name()

# Employee.location = "Mumbai"  #dynamically adding class attr

# def get_company_location(cls):
#     print("Company Location: ", cls.location)

# Employee.get_company_location = classmethod(get_company_location)

# del Employee.get_company_location

# emp.get_company_location()

# riya = Employee('Riya', 'Verma', 25)

riya = Employee.create_Employee_with_fullname("Riya Verma", 25)

# riya.get_details()
ravi = Employee.create_Employee_with_DOB("Ravi", 'Yadav', '12-07-1996')
ravi.get_details()
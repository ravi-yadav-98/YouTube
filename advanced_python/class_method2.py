'''
Classmethod in Python: @classmethod: part:02

-> A class method is bound to the class and not the object of the class.
-> It can access only class variables.
-> It can modify the class state.
-> The class method has a cls as the first parameter

ClassName.classMethod()

Usecases:

part:02
- factory method
- Singleton Design Pattern
- Classmethods in inheritance


'''

class Shape:
    
    def __init__(self, sides) -> None:
        self.sides = sides

    @classmethod
    def create_shape(cls, sides):
        if sides == 3:
            return Triangle(sides)

        elif sides == 4:
            return Square(sides)
        
        elif sides == 5:
            return Pentagon(sides)

        else:
            return Shape(sides)


class Triangle(Shape):
    pass

class Square(Shape):
    pass 

class Pentagon(Shape):
    pass


# triangle  = Shape.create_shape(3)   #object of Triangle class
# print(type(triangle))
# square   = Shape.create_shape(4)   
# print(type(square))


#Singlton Design Pattern: Creation DP

class DataBase:

    _instance = None
    count = 0

    def connect(self):
        pass

    def query(self):
        pass
    
    @classmethod
    def get_instance(cls):

        if cls._instance is None:
            cls._instance = cls()
            cls.count += 1
        return cls._instance

db1 = DataBase.get_instance()
# db2 = DataBase.get_instance()
# print(db1)
# print(db2)
# print(DataBase.count)



class Person:
    country = 'India'
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age
    
    @classmethod
    def get_country(cls):
        print("My Country is: ", cls.country)


class Student(Person):
    country = 'Nepal'
    def __init__(self, name, age, std) -> None:
        self.std = std
        super().__init__(name, age)


student = Student("A", 13, 5)

print(student.country)
student.get_country()
Student.get_country()
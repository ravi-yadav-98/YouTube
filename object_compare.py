'''
Object Comparison Methods Python:  How to compare two Objects in Python

Implement these magic methods to make object comparable


Magic methods:
__lt__()   : less than <
__gt__()   : greater than > 
__le__()   : less than equal to <=
__ge__()   : greater than equal to >=
__eq__()   : equal to ==

'''
# print(2 <10)
# print(12 ==10)

arr = [1, -1, 0, 9, 2, 10]
# print(sorted(arr))

class Student(object):
    def __init__(self, name, age, std):
        self.name = name
        self.age = age 
        self.std = std

    def __lt__(self, other):
        return self.age < other.age
    
    def __le__(self, other):
        return self.age <= other.age
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __ge__(self, other):
        return self.age >= other.age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __ne__(self, other):
        return self.age  != other.age
    
    def __str__(self):
        return f"Student({self.name}, {self.age}, {self.std})"


s1 = Student('A', 18, 12)  
s2 = Student('B', 17, 10)

students = [
    Student('A', 18, 12),
    Student('D', 12, 7),
    Student('C', 15, 9),
    Student('B', 9, 5),
    Student('P', 16, 11),
    Student('K', 12, 6)
]

print("unsorted list")
for student in students:
    print(student, end= ", ")

print(" ")
print(" ")
print("sorted list")
for student in sorted(students):
    print(student, end= ", ")

# print(sorted(students))

# print(s1 < s2)
# print(s1 == s2)
# print(s1 > s2)
# print(s1 <= s2)
# print(s1 != s2)
# print(s1 >= s2)







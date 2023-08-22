'''
Custom Sorting in Python: 

- How to make class Object comparable (To implement sorting)
- Custom Sorting: default Ordering 
- Custom Sorting : External method for sorting 
        comp_to_key


comparision methods: 
__lt__(), __le__(), __gt__(), __ge__(),
 __eq__(), __ne__()
'''
#Person Class : for Demo
#implmenet magic comparison methods to
#make objects comparable
class Person:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age
    
    def __str__(self):
        return f"{self.name} - {self.age}"
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __gt__(self, other):
        return self.age > other.age



#custom sorting: Flexible
from functools import cmp_to_key

def compare_person_on_name(person1, person2):
    if person1.name < person2.name:
        return -1
    elif person1.name > person2.name:
        return 1
    else:
        return 0

persons = [
    Person('John', 19),
    Person('Roy', 13),
    Person('Riya', 26),
    Person('Krish', 23),
    Person('Bob', 17), 
    Person('Mukesh', 15), 
    Person('Kriti', 27), 
]

# print(persons[0]  < persons[1])
for student in sorted(persons, key=cmp_to_key(compare_person_on_name)):
    print(student)


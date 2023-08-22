'''
Custom Sorting: Part:02
 - Other Ways to implement custom sorting

'''
from functools import cmp_to_key

names =[
    "Alice",
    'Jiya',
    'Bob',
    'Rameshwar',
    'Dave',
    'Karan',
    'Ajitesh'
]

def compare_on_length(s1, s2):
    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1
    else:
        return 0

# print(sorted(names, key = cmp_to_key(compare_on_length)))
# print(sorted(names, key = lambda s: len(s), reverse=True))


class Person:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age
    
    def __str__(self):
        return f"{self.name} - {self.age}"


persons = [
    Person('John', 19),
    Person('Roy', 13),
    Person('Riya', 26),
    Person('Krish', 23),
    Person('Bob', 17), 
    Person('Mukesh', 15), 
    Person('Kriti', 27), 
]

# for student in sorted(persons, key =lambda p: p.age):
#     print(student)


arr = [2, -4, 8, -3, 5, 4]
print(sorted(arr, key= lambda num: num**3))
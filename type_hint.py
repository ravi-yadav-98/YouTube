'''
Type Annotation/hinting in Python:  Typing Module:
Python versions: >= 3.5

Basics:

Two Types of Programming Languages:
1. Statically Typed: Data Types validated at compiletime : 
    i.e. c, c++, java, c#
    int a=2;

2. Dynamically Typed Language: Type checking at runtime
    i.e. Python, JavaScripts, PHP
    name = 'john'


Type Declaration advantage:
 - Improvde Code Readibility
 - Clean and Maintaiable code/Debugging 
 - Easy Documentation and Docstring


 Static Type Checker Tool: mypy
 > pip install mypy

 
 Content: 
  - Variable Type Anotation/Checking
  - Any Type 
  - Function Annotations(parameter/return)
  - Type Aliases
  - User Defined Data Types
  - 

'''

from typing import *

# name:str = "ravi"
# print(name


#  -  Variable Type Anotation/Checking
name:str = "ravi"
# print(name)

num:float = 1.2
lst:list  = [1,2,3,4]
mydict:dict = {'a':2, 'b':2}
num1:int = 12


#   - Any Type 
var:Any = 10

#   - Function Annotations(parameter/return)

def get_user_info(name:str, age:int, salary:float,
                  is_Indian:bool = True) -> str:
    
    info = f'''
    name: {name}\n
    age: {age}\n
    salary:{salary}\n
    is_India:{is_Indian}
    '''
    return info

# print(get_user_info("ravi", 26, 60000))
# print(get_user_info.__annotations__)



#   - Type Aliases

vector = List[int]
map    = Dict[str, int]

list_tuple = List[Tuple[str, int]]

def print_vector(lst:List[int]) -> List[int]:
    return lst*2

#print(print_vector([1,2,3,4,"2"]))


#   - User Defined Data Types

userId = NewType('userId', int)

def get_userId(userid: userId) -> userId:
    return userid

user_id : userId = userId(123)
print(user_id)
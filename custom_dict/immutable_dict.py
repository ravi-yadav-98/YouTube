'''
Immutable Dict: Customized Dict Class/User Defined
    a dictionary that does not allow its keys or values 
    to be changed after initialization.

    - Can't update, delete, add value etc.
    - Modify as you need


Example: Student's marks dict

UserDict:
    field: data
    Methods:
         __getitem__()
         __setitem__()
         __popitem__()
         __del__()
         pop()
         update()
         clear()

'''

from collections import UserDict

class ImmutableDict(UserDict):
    
    def __setitem__(self, key, val):
        raise RuntimeError("Immutable Dict, Can't modify")
    
    def popitem(self):
        raise RuntimeError("Immutable Dict, Can't modify")

    def pop(self, key):
        raise RuntimeError("Immutable Dict, Can't modify")

    # def update(self, *args, **kwargs):
    #     raise RuntimeError("Immutable Dict, Can't modify")
    
    def clear(self):
        raise RuntimeError("Immutable Dict, Can't modify")
    
  



#Driver's Code

if __name__ =='__main__':

    student_marks = {
        "Alice": 85,
        "Bob": 78,
        "Ravi": 62,
        "David": 68,
        "Riya": 95
    }

    my_dict = ImmutableDict(student_marks)

    print(my_dict['Alice'])
   
    



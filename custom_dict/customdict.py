'''
Custom dictionary in Python:

UserDict class:
field: 
    data: dict
Methods:
  __getitem__(key) :  to get value of key
  __setitem__(key, val)  : to set key, value pair


UseCase:
1. Key CaseInsensetive Dictionary
2. Default Dictionary

'''
from collections import UserDict
# print(help(UserDict))


class CaseInsensitiveDict(UserDict):
    
    def __init__(self):
        super().__init__()
    
    def __setitem__(self, key, value ):
        self.data[key.lower()] = value
    
    def __getitem__(self, key):
        return self.data[key.lower()]



#create Obj
num_dict = CaseInsensitiveDict()

# num_dict['One'] = 1 #setime
# num_dict['Two'] = 2
# num_dict['Three'] = 3
# num_dict['Four'] = 4

# # print(num_dict)
# print(num_dict['fouR'])





class DefaultDict(UserDict):
    def __init__(self, default_val = None):
        super().__init__()
        self.default_val = default_val


    def __getitem__(self, key):
        if key not in self.data:
            return self.default_val
        return self.data[key]
    
    def pop(self, key = None):
        raise RuntimeError("You Can not delete item.. ")

    

   
    

my_dict = DefaultDict(-1)
my_dict['One'] = 1 #setime
my_dict['Two'] = 2
my_dict['Three'] = 3
my_dict['Four'] = 4
my_dict.pop('One')
print(my_dict)

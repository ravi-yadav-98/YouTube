'''
Restricted Dict: Custom Dict
:  a restricted dictionary that allows you to define specific keys that can be 
modified while preventing modification of other keys

: user can modify  speficied keys


- can be useful in various scenarios where you want to control
and enforce restrictions on the usage of a dictionary.

Example:
    
    - User Profile:  as a specific format

    {
        Firstname:
        LastName:
        Email:
        Phone:
        DOB: 
    }

    - Setting Configuration(text Editor)
    {
        font-size:
        theme:
        tab-size:
        auto-save
        word-wrap

    }


UserDict class
    - field: data(dict)
    __setitem__()
    __getitem__()
    __delitem__()

    pop()
    update()
    clear()
    popitem()



    
'''

from collections import UserDict

class RestrictedDict(UserDict):
    def __init__(self,  allowed_keys):
        self.allowed_keys = allowed_keys
        super().__init__()
    
    def __setitem__(self, key, val):
        if key in self.allowed_keys:
            super().__setitem__(key, val)
        
        else:
            raise KeyError(f"{key} is not allowed")
    
    def __delitem__(self, key):
        if key in self.allowed_keys:
            super().__delitem__(key)

        else:
            raise KeyError(f"{key} is not allowed")
    
    def pop(self, key):
        if key in self.allowed_keys:
            super().pop(key)
        
        else:
            raise KeyError(f"{key} is not allowed")
    
    def clear(self):
        raise NotImplementedError("Clear() function is not allowed")
    

    def update(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.allowed_keys:
                  raise KeyError(f"{key} is not allowed")
        
        super().update(**kwargs)



#Driver's Code

if __name__ == '__main__':
    allowed_keys = ['name', 'lastname', 'email', 'phone', 'DOB']

    my_dict = RestrictedDict(allowed_keys)
    my_dict['name'] = 'ravi'
    print(my_dict)

    try:
        my_dict['interest'] = 'cricket'
    except:
        print("Now Allowed")
    
    my_dict['lastname'] = 'yadav'

    try:
        my_dict['age'] = 26
    except:

        print("Now Allowed")
    
    my_dict.pop('name')
    # my_dict.pop('age')
    print(my_dict)
    my_dict.clear()
 
   



'''
Expiring Key Dictionary (Cache Like): Custom Dictionary
    - dictionary that automatically expires keys after a certain duration
    - cache-like dictionary

    ex: OTP Verification system
    cache_dict: {num1: 11, num2: 5: num3: 10}




UserDict
    field -> data(dict)
    methods:
        - __getitem__()
        - __setitem__()
        - __contains__()
        - pop()
    
'''

from collections import UserDict
import time

#Expiring key Dictionary
class CacheLikeDict(UserDict):
    
    def __init__(self, expire_time = 10):
        super().__init__()
        self.expire_time = expire_time
        #key entry time record
        self.time_data = {}
    
    def __setitem__(self, key, val):
        add_time = time.time()
        self.data[key] = val
        self.time_data[key] = add_time
    

    def __getitem__(self, key):
        get_time = time.time()

        if  key in self.time_data and get_time - self.time_data[key] >= self.expire_time:
            del self.data[key]
            del self.time_data[key]

            raise KeyError(f"{key} has expired !! ")
        return self.data[key]




#driver's code

if __name__ == '__main__':

    my_dict =  CacheLikeDict(expire_time=15)
    my_dict['key1'] = 10
    my_dict['key2'] = 15
    my_dict['key3'] = 100
    my_dict['key4'] = 21
    print(my_dict)
    time.sleep(6)
    try:
        print(my_dict['key1'])
    except:
        print("KEY has Expired!")
'''
Types of Dictionies in Python:

key-Value pair

Dictionary Types in Python
1. Dict: unordered dictionary (Can not handle missing keys)
2. Default dict : Handle missing Keys
3. ordered dict : Ordered dict(python  < v3.7) : memory wastage                    
4. user dict    : easy Sub-classing, adding new methods to dict class(wrapper)


'''
#import modules
from collections import defaultdict, OrderedDict, UserDict

#1. dict
my_dict = dict()

my_dict['one']   = 1 
my_dict['two']   = 2
my_dict['three'] = 3 
my_dict['four']  = 4
my_dict['five']  = 5
# try:
#     print(my_dict['six'])
# except:
#     print("Key not found")
# print(my_dict)

#2. default dict

my_default_dict = defaultdict(lambda: "Key Not Found")

my_default_dict['one']   = 1 
my_default_dict['two']   = 2
my_default_dict['three'] = 3 
my_default_dict['four']  = 4
my_default_dict['five']  = 5

# print(my_default_dict['six'])




#3. ordereddict
my_ordered_dict = OrderedDict()

my_ordered_dict['one']   = 1 
my_ordered_dict['two']   = 2
my_ordered_dict['three'] = 3 
my_ordered_dict['four']  = 4
my_ordered_dict['five']  = 5
# print(my_ordered_dict)




# 4. user dict

my_user_dict = UserDict(my_dict)    #takes dict as input
print(my_user_dict.data)





















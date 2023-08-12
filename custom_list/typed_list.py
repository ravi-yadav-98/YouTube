'''
Custom List: using List -SubClassing 

Python List Properties:
 - Ordered
 - Heterogeneous
 - Mutable

Why Custom List: 
    Some Special use cases
       Typed List, Logging List, Data Transformation
        SortedList, RestrictedList


Prerequisites: Python OOps

Python Major Functions: 
 - append()
 - count()
 - insert()
 - extend()
 - pop()
 - remove()
 - index()
 - 

'''
# print(help(list))

l = list([1,2,3,4])

#This Video: Typed List, 

class TypedList(list):
    def __init__(self, dtype= object):
        self.dtype = dtype 
        super().__init__()
    
    def append(self, value):
        if isinstance(value, self.dtype):
            super().append(value)
        
        else:
            raise ValueError(f" Only {self.dtype.__name__} can be added..")
    

myTypedList = TypedList(str)
# myTypedList.append(10.2)
# myTypedList.append(20.3)
# myTypedList.append(30.8)
# print(myTypedList)
try:
    myTypedList.append(10)
except:
    print("Can not be added..")

myTypedList.append("Ravi")
print(myTypedList)

#We have not overridern insert function
myTypedList.insert(0, 10)
print(myTypedList)

'''
Homework:
 - Override insert and extend function of list in Typed List
'''
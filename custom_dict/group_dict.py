'''
Custom Dictionary: Group Dict

Dictionary that group data based on similarity: Data Aggregation 

Ex:
{
    group1 :[ val1, val2]
    group2 :[ val3, val4]
    group2 :[ val4, val4]
}

UserDict
    field -> data(dict)
    methods:
        - __getitem__()
        - __setitem__()
        - pop()
'''

from collections import UserDict
class GroupDict(UserDict):
    def __init__(self):
        super().__init__()
    
    
    def __setitem__(self, key, val):

        if key not in self.data:
            self.data[key] = []
        
        self.data[key].append(val)



#driver's code
if __name__ == '__main__':

    mydict = GroupDict()

    mydict['animal'] = 'dog'
    mydict['animal'] = 'cat'

    mydict['country'] ='India'
    mydict['country'] ='Nepal'
    mydict['country'] ='Canada'

    mydict['color'] = 'red'
    mydict['color'] = 'pink'
    mydict['color'] = 'blue'

    mydict["number"] = 10
    mydict["number"] = 11

    print(mydict)


'''
Custom List: using List -SubClassing 

Today's Video: Sorted List
 - A List that place elements in sorted order
 Ex: Priority-Queue DS

[1,10, 20, 4] -> [1,4,10, 20]

Prerequisites: Python OOps

Python Major Functions: 
 - append()
 - insert()
 - extend()
 - pop()
 - remove()
'''

import sys
sys.setrecursionlimit(2800)

class SortedList(list):
    def __init__(self):
        super().__init__()

    def insert_sorted(self, value):
            left, right = 0, len(self)
            while left < right:
                mid = (left + right) // 2
                if self[mid] < value:
                    left = mid + 1
                else:
                    right = mid
            self.insert(left, value)
    def append(self, value):
        self.insert_sorted(value)

    def insert(self, index, value):
        self.insert_sorted(value)

    def extend(self, iterable):
        for value in iterable:
            self.insert_sorted(value)
    

myList = SortedList()
myList.append(10)
myList.append(1)
myList.append(-2)
myList.append(21)
myList.append(5)
print(myList)
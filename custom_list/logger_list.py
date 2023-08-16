'''
Custom List: using List -SubClassing 

Today's Video: Logger List
 - Record history of all the operation happening on List

 i.e. time, event, value


Prerequisites: Python OOps

Python Major Functions: 
 - append()
 - insert()
 - extend()
 - pop()
 - remove()

'''
from collections.abc import Iterable
from datetime import datetime

class LoggerList(list):
    
    def __init__(self):
        super().__init__()
        self.history = []
    

    def log_history(self, action, **kwargs):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.history.append({
            'time': timestamp,
            'action': action,
            **kwargs

        })
    def append(self, value):
        self.log_history("append", value=value)
        return super().append(value)

    def pop(self, index=-1):

        pop_value = super().pop(index)
        self.log_history("pop", value = pop_value)
        return pop_value
    
    def remove(self, value):
        super().remove(value)
        self.log_history("remove", value=value)
    

    def insert(self, index, value):
        super().insert(index, value)
        self.log_history("insert",index = index, value=value)
    
    def extend(self, iterable):
        super().extend(iterable)
        self.log_history("extend", iterable = iterable)
    
    def get_history(self):
        for log in self.history:
            for (key, value) in log.items():
                print(key, value, end=" ")
            print(" ")
            
           
    


import time
if __name__ == '__main__':
    logger_list = LoggerList()
    logger_list.append('Ravi')
    logger_list.append(18)
    logger_list.extend([1,2,3])
    logger_list.pop()
    logger_list.pop(3)
    time.sleep(2)
    logger_list.insert(0, "Hello")
    print(logger_list.get_history())
    print(logger_list)

    
    

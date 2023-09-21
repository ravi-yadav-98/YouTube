'''
String Interning: 
The string interning in Python is a mechanism of storing only one copy of a string value in the memory.

-> Multiple varible will refer to same object
-> Memory Saving

How interning orrurs:
 - Depend on python version

#Explicit Interning: sys.intern()

Advantage:
 - Memory Optimization
 - Fast String Comparison ( is faster than ==)

Drawback:
 - It will take time to take time to intern long string

'''

s1 = 'Hello World'*100
s2 = 'Hello World'*100    

# print(hex(id(s1)))
# print(hex(id(s2)))
# print(s1 is s2)  #faster
# print(s1 == s2)   #slow


import sys 
import time

var1 = sys.intern("I am leanring python")
var2 = "I am leanring python"
# print(var1 is var2)




def compare_strings():

    d = 'I am Learning Python Programming'*100000
    e = 'I am Learning Python Programming'*100000
    for i in range(100000):
        if d is e:
            pass

start = time.time()
compare_strings()
end = time.time()

print("Execution time: ", end - start, 'sec')



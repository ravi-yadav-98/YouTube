'''
Mutable and Immutable Objects in Python:

Immutable:
 - Immutable objects are those whose values cannot be changed after they are created(In-memory)
 - When you attempt to modify an immutable object,
 Python creates a new object with the modified value

 ex: int, float, string, Tuple,

 or Classes with immutable attributes


Mutable:
Mutable objects are those whose values can be changed after they are created.
 When you modify a mutable object, the changes are reflected in the same object,
 and its identity (memory location) remains the same.

 ex: List, Dict, Sets, or Classes with mutable attributes



'''

#Immutable objects

# value = 10
# print('original id: ', id(value))
# value = value +1
# print('new id: ', id(value))

# s = 'abc'
# print('original id of s: ', id(s))
# s += 'd'
# print('new id of s: ', id(s))


#mutable objects

arr = [1,2,3,4, [10,20]]  #1007[106, 108, 1012, 2884]
# print('arr original id: ', id(arr))
# for a in arr:
#     print(f'id of {a}: ', id(a))

arr.append(12)
# print('arr new id: ', id(arr))

# for a in arr:
#     print(f'id of {a}: ', id(a))

print('id of index 1 value:  ', id(arr[4]))
arr[4].append(30)
print('id of index 1 value:  ', id(arr[4]))

























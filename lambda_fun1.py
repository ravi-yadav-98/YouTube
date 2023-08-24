'''
Lambda Function in Pyhon: Part: 01 basci usecases

concise way to define small, anonymous functions using a compact syntax.


Pros:
- Conciseness
- Functional Programming
-  Inline Uses
- No need of Function overhead


cons:

They can only contain a single expression.
They cannot include statements or multiple expressions.
They are less readable for complex operations.
No Documentation, Docstrings
'''

    

square = lambda num : num**2

# add = lambda x, y, z : x+y-z

# print(add(1,2))

#custom sorting 

arr = ['Banana', 'Cherry', 'Mango', 'pear', 'Apple']

# print(sorted(arr, key=lambda s: s[-1]))

points = [(3, 4), (1, 2), (5, 1), (-1, 2), (0, -2)]
# print(sorted(points, key =lambda el: el[0] ))


def modifier(func, num):
    return func(num)


inc_4 = lambda x : x+4

print(modifier(lambda x : x/10, 10))



lst = [1,2,3,4,5]

cubes = list(map(lambda x: x**3, lst))
# print(cubes)

even = list(filter(lambda x: x%2==0, lst))
print(even)



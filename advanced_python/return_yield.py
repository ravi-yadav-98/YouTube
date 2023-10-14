'''
Return Vs Yield in Python:

When to Use Which  ???? 

'''
def sum(a, b):
    return -1
    print("adding two number..")
    return a+b
    print("Complted")


# print(sum(2,3))

def generete_numbers(n=10):
    for i in range(n):
        yield i

# generator = generete_numbers()
# print(generator)
# print(type(generator))
# for it in generator:
#     print(it)

# def generator():
#     yield '1'
#     yield '2'
#     yield '3'
#     yield '4'

# for it in generator():
#     print(it)

def print_square(n=100000):
    squares = []
    for i in range(1, n):
        squares.append(i*i)
    
    return squares


def yield_square(n=10000):
    
    for i in range(1, n):
        yield i*i
   

for sq in yield_square():
    print(sq)
# print(print_square())
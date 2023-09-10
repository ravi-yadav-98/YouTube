'''
Variable Length arguments:  *args and **kwargs

args variable: varying number of arguments(positional)
kwargs: keyword arguments

To pass optional arguments to functions/methods
-> Create flexible modules/classes
-> Arbitrary arguments

Type of arguments:
1. Positional
2. Keyword Arguments
3. Default Arguments
4. Optional Arguments

'''

def print_sum(presum, *args):
    # print('a: ',  a)
    # print('b: ',  b)
    # print('c: ',  c)
    print(type(args))
    sum = presum
    for num in args:
        sum += num
    print('sum: ', sum)

# print_sum(10, 12, 20)


def get_user_info(name, age, **kwargs):
    print("user details: ")
    print('name:', name)
    print('age: ', age)

    if kwargs:
        for key, val in kwargs.items():
            print(key, ' : ',  val )

get_user_info('Amit', 23, email ='amit123@gmail.com', salary=12000)


class Person:
    def __init__(self,name, age,  *args, **kwargs):
        self.name = name
        self.age = age
        










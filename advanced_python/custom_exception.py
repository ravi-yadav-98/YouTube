'''
Custom Exception in Python:

Exception: Runtime Error
 - Error which occurs during the execution of a program that
 disrupts the normal flow of the program


Builtin Exceptions:
 - ValueError, TypeError, IndexError
 - KeyError, ZeroDivisionError:
 - Import Error

'''

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("Can't divide with zero")
# print("hello")

# class CustomException(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
# x = 2
# if x<2:
#     print("hello")
# else:
#     raise CustomException("Custom Exception")


class PasswordTooShort(Exception):
    '''
    Custom Exception for Password validation
    '''
    def __init__(self, message):
        super().__init__(message)

def generate_password(password):

    if len(password) >=8:
        print("Password Generated Successfully")
    else:
        raise PasswordTooShort("Password must be of length 8")

# try:
#     generate_password('ravi233323')
# except PasswordTooShort as msg:
#     print(msg)


class MaxApiCallExceeded(Exception):
    def __init__(self, message):
        super().__init__(message)



def sampleAPI(limit):
    if limit <=5:
        print('API called success ')
    else:
        raise MaxApiCallExceeded("max api call exceeded..")


for i in range(1, 10):
    print('Call number: ', i)
    sampleAPI(i)

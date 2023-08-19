'''
Context Manager In Python:  With Statement

-  automatically allocating and releasing those resources within a specific context. 
- ex: files read/write, connections

usecase:
1. read write file automatically Open()
2.OS.chdir()
3. Lock() in Threading Module
4. Socket/Database Connection


Note:
To implement a context manager, you need to define a 
class with two special methods: __enter__() and __exit__(). The __enter__() 
method is responsible for setting up the resource or environment, while the __exit__() 
method is responsible for cleaning up and releasing the resource.

'''

#file

# file = open("test.txt", 'w')


# # file.close()

# try:
#     file.write("Writing without context manager")
# finally:
#     file.close()


#with context manager

with open('test2.txt', 'w') as file:
    file.write("Writing with context manager")



# import threading 


# lock = threading.Lock()

# lock.acquire()
# print("hello")

# lock.release()


class FileManager:
    def __init__(self, filename) -> None:
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exe_tb):
        if self.file:
            self.file.close()


with FileManager('hello.txt') as f:
    f.write("Custom Context Manager")


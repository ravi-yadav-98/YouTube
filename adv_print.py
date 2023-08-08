import time
"""Print Function Advance Features """

# print(help(print))

#contents: 
#1 end and sep parameter
# print(1,2,3,4,5, sep='/ ')
# print("Hi", end =', ')
# print("How are u ")

#2 Flush Parameter
# print("Hello, ", end ='', flush=True)
# time.sleep(3)
# print("How are you ??")
# print("I am fine")

#3 print to file
# print("Hi, I am Ravi", file = open("out.txt",'w'))

# with open("output.txt", 'w') as file:
#     print("Hi, How are you ? ", file =file)
#     print("I am fine", file =file)
#     print("How about you ? ", file =file)

#4 Print Formatting (format , f-string)
# name = input("Enter your name. ")
# age = input("Enter Your age.. ")

#format
# print("My name is {0}. I am {1} years old".format(name, age))

#f-string
# print(f"My name is {name}. I am {age} years old")

#5 Show progress using print

for i in range(10):
    time.sleep(1)
    print(f"\rProcess Completed {i+1}/10", end ="")


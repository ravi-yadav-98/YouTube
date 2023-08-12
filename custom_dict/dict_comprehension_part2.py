'''
Part:02 Advances uses of Dict Comprehension

Dictionary Comprehension in Python: 
   - Dictionary comprehension is a concise and efficient way to create/modify dictionaries in Python
  - used to substitute for loops and lambda functions


'''

#1. Lambda Exression with Dict Comprehension

nums = [1,2,3,4,5,6,7,8,9]

print({num: "even" if num%2==0 else 'odd' for num in nums })


data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 10},
    {'name': 'Charlie', 'age': 22}
    {'name': 'john', 'age': 12}
]

print({})


#2: dictionary of functions

#3.Merging Two Dictionaries( different ways)

#4. Working with complex(nested dict)

#5  Creating a Dictionary from a File:

#6 Dict of Custom Objects



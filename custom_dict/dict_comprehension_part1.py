'''
Part:01 Basics:

Dictionary Comprehension in Python: 
   - Dictionary comprehension is a concise and efficient way to create/modify dictionaries in Python
  - used to substitute for loops and lambda functions


'''

#Content:

#1 Ways to Iterate over a Dict:(key, value, pair, enumerate)
# name_age = {
#     'Alice': 25,
#     'Bob': 30,
#     'Charlie': 22,
#     'David': 28,
#     'Eve': 24,
#     'Frank': 35,
#     'Grace': 29,
#     'Helen': 31
# }

#keys
# for key in name_age.keys():
#     print(key," -> " ,name_age[key])

#values
# for val in name_age.values():
#     print(val)

# for (key, value) in name_age.items():
#     print(key , " - " , value)

# for idx, (key, val)  in enumerate(name_age.items()):
#     print("Id-", idx, " ", key, " ", val)



#2. Create Dictionaries from List (Mapping)
keys = ['name', 'age', 'city', 'hobby']

values =['ramesh', 24, 'chennai', 'music']

#for loop
data = {}
# for i in range(len(keys)):
#     data[keys[i]] = values[i]

# print(data)
# for key, val in zip(keys, values):
#     data[key] = val
# print(data)


#Dict comprehension:

data = {key: val for key, val in zip(keys, values)}
# print(data)


#3. Working With simple Dict Comprehension

# new_dict = {key.lower(): val+10 for key, val in name_age.items()}
# print(new_dict)

#revere

# reverse_dict ={val:key for key, val in name_age.items()}
# print(reverse_dict)

#char count

s = "hello how are you"
# print({word: len(word) for word in s.split(" ")})


word = "Apples"
# print({c: word.count(c) for c in word})


#4:Conditional Dict Comprehension (if else )


name_age = {
    'Alice': 25,
    'Bob': 30,
    'Charlie': 22,
    'David': 28,
    'Eve': 24,
    'Frank': 35,
    'Grace': 29,
    'Helen': 31
}


# print({key:val for key, val in name_age.items() if val > 25})


nums = [1,2,3,4,5,6,7,8,9,10]

# print({num: num**2 for num in nums if num%2==0})

#5 Using Lambda expression in dict comprehension

print({num:(lambda x: x**2)(num) for num in nums if num%2==0})


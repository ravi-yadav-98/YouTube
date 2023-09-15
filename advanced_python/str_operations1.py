
'''
Basic String Operations:

1. String Split
2. String Concatenation
3. String join

'''
#Split
text = 'Today, I am   learning Python Programming.'
# words = text.split() #sep= ' ' -> remove extra spaces

words = text.split(maxsplit=2)
# print(words)

date = '21-March-2023'
# date_split = date.split('-', maxsplit=1)
# print(date_split[1])


#Concatenation

# s = 'Hello'
# s = s + ' World'

# s = s + str(2)

# s = 'a'*10
# print(s)

# s1 = 'abc'   # s1  ->   (2167251970096)'abc'
# print('original str id: ' , id(s1))
# s1 = s1 + 'd'   #s1 ---> 'abcd' (2167254119088)
# print('modified str id: ' , id(s1))
# print(s1)



#join
words = ['I', 'am', 'learning', 'Python']
date_sep = ['12', 'June', '2023']
# s = '-'.join(words)

date = '/'.join(date_sep)
print(date)







'''
Bisect Module In Python: 

The bisect module in Python provides support for maintaining a sorted list
and efficiently inserting elements while keeping the list sorted.

It utilizes a binary search algorithm to achieve this efficiency.


Methods:
#get index of value in sorted list
bisect.bisect():  first occurance
bisect.bisect_left(): last occurance
bisect.bisect_right():   same as bisect.bisect()

#insort: put at sorted pos

bisect.insort(): add at right side (if already present)
biset.insort_left(): add at left (if already present)
bisect.insort_right() : same as bisect.insort()

'''
import bisect

arr = [-7, 1, 4, 5, 7 ,7,7, 8 ,13, 21, 31, 38]

val = 7

# sorted_index = bisect.bisect(arr, val)

#left part
sorted_index_left  = bisect.bisect_left(arr, val)
sorted_index_right = bisect.bisect_right(arr, val)

# print("left pos: ", sorted_index_left)
# print("right pos: ", sorted_index_right)
# bisect.insort_left(arr, 7)
# print(arr)

arr2 = []
bisect.insort(arr2, 10)
bisect.insort(arr2, 1)
bisect.insort(arr2, 101)
bisect.insort(arr2, -10)
bisect.insort(arr2, 0)
bisect.insort(arr2, 108)
bisect.insort(arr2, 7)
print(arr2)





# Numbers, string, boolean, list, tuples, set, dictionary

# The type function is used to inspect the type of the object

# print(type('python'))

# Mutable and immutable objects
# - Mutable objects can be changed after they are created. e.g list, set, dictionary
# - Immutable objects can't be changed after they are created. e.g int, float, string, boolean, tuple

# Mutable
# list = ['apple', 'orange', 'banana']
# print(list)
# list[2] = 'strawberry'
# print(list)

# Immutable
# tuple = ('red', 2, 'green')
# tuple[2] = 'white'
# print(tuple)

# list append
# list = [1,2,3,4,5]
# list.append(6)
# print(list)
# list2 = [7,8]
# list.extend(list2)
# print(list)
#
# list.insert(0,5)
# print(list)
#
# list.remove(2)
# print(list)
# list.pop(2)
# print(list)
#
# # list.clear()
# # print(list)
#
# print(list.index(6))
# print(list.count(5))
# print(list.sort(reverse=True))
# print(list.reverse(1,2,3,5,8,9,6))

# List comprehension

# for x in range(5):
    # print(x)

# Strings

# s = 'Hello world'
# for i in s[2:5]:
#     print(i)
# a = ''
# b = 'world'
#
# print(bool(a))

# a = 'hello world'
# print(a.capitalize())
# print(a.islower())
# print(a.upper())
# print(a.split('o'))
# print(a.title())
#
# str1 = 'Cookie cutter'
# str2 = 'utt'
# str3 = 'Cut'
# print(str1.find(str2))
# print(str1.find(str3))
# print(str1.replace('oo', 'OO'))

# Formatting:

# a = 'I\'m %s and I\'m %d years old'%('Dorje Tshering Sherpa', 25)
# print(a)

# %d - integer , %f - float, %s - string, %.2f - float with 2-digit floating point, %.4f - float with 4-digit floating point

# Format method:
# a = "I'm {name}.\t".format(name = 'Dorje Tshering Sherpa')
# b = "and I'm {} years old".format(25)
# print(a+b)

# Format method- Postional arguments:

# a = "I've {1}, {2}, {0}.".format('book','pen','copy')
# print(a)
# possible errors - 1. If more placeholder are given than the paremeters. 2. If more arguments are given than the placeholders.
# 3. Can't mix the manual field specification and automatic field numbering techniques together. like
# a = '{1}, {2}, {} are fun to learn'.format('Python', 'Django', 'Java')
# print(a)

# F-strings:
# name = "Dorje Tshering Sherpa"
# print(f"Hi! {name}")

# Multi f-line strings:
# name = "Dorje Tshering Sherpa"
# age = 25
# work = "Computer Engineer"
# print(f"Hi! {'Dorje'}. " f"You are {age} years old. " f"You're a {work}.")

# Boolean Type: Any list, tuple, set and dictionary are True, except empty ones.
# bool value of False, None, 0 are false
# true = 1 and false = 0
# print(False + 2)
name = 'Dorje'
print(bool(name))
print(bool(0))
print(bool(1))

# Development tools: inspect garne ani herne sabai tya vako change garna milcha but only for the time being.

# Tuples: it is a collection made from (). Unlike lists, tuples are immutable.

# a = ()
# print(type(a))

tup1 = ('Dorje', 'Tshering')
print(tup1)

tup2 = 'Dorje', 'Tshering'
print(tup2)

# Tuples support mixed types.e.g
a = ('John', 2)
print(a)

# Also tuple can be a nested tuple
b = ('a', 'g', ('abc',2,3), [1,5,6])
print(b)

mytuple = tuple('Hello')
print(mytuple)

# integer is not iterable unlike list and string and packing and unpacking , packing means getting a tuple into a (), and
# unpacking is done to not keep it together.

# Tuple unpacking:
# g = ('john', 'writer', 23)
# name, profession, age = g
# print(g[1])
# to delete a tuple:
# del g

d = (5,6,7,8,9,4,5)
print(d.index(5, 2))
print(sorted(d))
print(reversed(d))
print(list(reversed(d)))

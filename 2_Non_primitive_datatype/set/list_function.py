# First way: using the set() function on an iterable object
set1 = set([1, 1, 1, 2, 2, 3])     # from a list
set2 = set(('a', 'a', 'b', 'b', 'c'))  # from a tuple
set3 = set('anaconda')         # from a string

# Second way: using curly braces
set4 = {1, 1, 'anaconda', 'anaconda', 8.6, (1, 2, 3), None}

print('Set1:', set1)
print('Set2:', set2)
print('Set3:', set3)
print('Set4:', set4)

set5 = {1, 1, 'anaconda', 'anaconda', 8.6}
print('Set5:', set5)

# output 
# Set1: {1, 2, 3}
# Set2: {'b', 'c', 'a'}
# Set3: {'a', 'd', 'n', 'o', 'c'}
# Set4: {None, 1, 'anaconda', 8.6, (1, 2, 3)}
# Set5: {8.6, 1, 'anaconda'}

empty1 = {}
empty2 = set()

print(type(empty1))
# <class 'dict'>

print(type(empty2))
# <class 'set'>

myset = {1, 2, 3}
print(1 in myset)  # True

print(1 not in myset)  # False

# accessing value from set
myset = {'a', 'b', 'c', 'd'}

for item in myset:
  print(item,end=" ") # d b c a
  
# Modifying a Python Set, adding items 
myset = set()

print()
# Adding a single immutable item
myset.add('a')
print(myset)  #  {'a'}

# Adding several items
myset.update({'b', 'c'})    # a set of immutable items
print(myset)    #  {'b', 'c', 'a'}

myset.update(['d', 'd', 'd'])  # a list of immutable items
print(myset)    #  {'b', 'c', 'a', 'd'}

myset.update(['e'], ['f'])   # several lists of immutable items
print(myset)    #    {'c', 'f', 'e', 'a', 'b', 'd'}
myset.update('fgh')       # a string
print(myset)    #    {'h', 'c', 'f', 'g', 'e', 'a', 'b', 'd'}
# removing item from list

myset = {1, 2, 3, 4, 6, 8}
print(myset)    #  {1, 2, 3, 4, 6, 8}

# Removing a particular item using the discard() method

myset.discard(1) # the item was present in the set
print(myset)  #  {2, 3, 4, 6, 8}

myset.discard(5) # the item was absent in the set
print(myset)  #  {2, 3, 4, 6, 8}

# Removing a particular item using the remove() method
myset.remove(4)  # the item was present in the set
print(myset)  #  {2, 3, 6, 8}


# the removed and returned item
print(myset.pop()) # the removed and returned item # 2
print(myset)    # the updated set  #{3, 6, 8}

        
# An attempt to remove and return a random item from an empty set
myset.pop()
print(myset)  #{6, 8}


# Removing all the items
myset.clear()
print(myset)  #set()

# A set with numeric items
myset = {5, 10, 15}
print('Set:', myset)
print('Size:', len(myset))
print('Min:', min(myset))
print('Max:', max(myset))
print('Sum:', sum(myset))
print('\n')

# A set with string items
myset = {'a', 'A', 'b', 'Bb'}
print('Set:', myset)
print('Min:', min(myset))
print('Max:', max(myset))
print('\n')

# A set with tuple items
myset = {(1, 2), (1, 0), (2, 3)}
print('Set:', myset)
print('Min:', min(myset))
print('Max:', max(myset))

print(all({1, 2}))
print(all({1, False}))
print(any({1, False}))
print(any({False, False}))

myset = {4, 2, 5, 1, 3}
print(sorted(myset))

myset = {'c', 'b', 'e', 'a', 'd'}
print(sorted(myset))
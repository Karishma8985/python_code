

#Performing Mathematical Set Operations on Python Sets
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}
#union

#   The union of two (or more) Python sets returns a new set of all the unique items from both (all) sets. It can be performed using the | operator or the union() method

print(f"a | b: {a | b}")
print(f"b | a: {b | a}")
print(f"a.union(b): {a.union(b)}")
print(f"b.union(a): {b.union(a)}")

print()


#intersection


print(f"a & b: {a & b}")
print(f"b & a: {b & a}")
print(f"a.intersection(b): {a.intersection(b)}")
print(f"b.intersection(a): {b.intersection(a)}")

print()
#difference
print(f"a - b: {a - b}")
print(f"b - a:  {b - a}")
print(f"a.difference(b):{a.difference(b)}")
print(f"b.difference(a): {b.difference(a)}")

print()
# set Symmetric Difference
print(f"a ^ b: {a ^ b}")
print(f"b ^ a: {b ^ a}")
print(f"a.symmetric_difference(b): {a.symmetric_difference(b)}")
print(f"b.symmetric_difference(a): {b.symmetric_difference(a)}")
# tuple means same as list but immutable(not changeable)
#  Tuples are used to store multiple items in a single variable
# tuple is a collection of different kinds of datatype, ordered, indexed but cant changeable.....

# it is denoted by ()

tuple = (100, 200)
print(tuple[0])
print(tuple[1])

# tuple[0] = 150
            # show error in code
            #  tuple[0] = 150
            #     ~~~~~^^^
            # TypeError: 'tuple' object does not support item assignment


tup = (300, 250)
print(tup+tuple)  # concatenation of two tuple (joining)

jane = ("Jane Doe", 25, 1.75, "Canada")
point = (2, 7)
pen = (2, "Solid", True)

# use count() to count element
days = ("Monday","Monday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(days.count("Monday"))




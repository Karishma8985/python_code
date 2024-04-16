# A for loop is used for iterating (repeating)
# over a sequence (that is either a number, a list,
# a tuple, a dictionary, a set, or a string).
# example 1: list

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print('-'*30) 

# example 2:  string
for x in "Pythoncode":
    print(x,end=" ")

print()
print('-'*30) 

#The range() Function
# To loop for a series of specific number of times, we can use the range() function,
# starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# syntax is range(start,end,gap)

for i in range(10):
    print(i,end=" ")

print()
print('-'*30) 


for i in range(1,101):
    print(i,end=" ")

print()
print('-'*30) 

for x in range(2, 30, 3):
    print(x,end=" ")
  
print()
print('-'*30) 

# program for even no
for i in range(1,101):
    if(i%2==0):
        print(i,end=" ")

print()
print('-'*30) 

t=tuple(x**2 for x in range(11))  # (0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(f"square : {t}")


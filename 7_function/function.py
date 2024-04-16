# function with no argument
def my_function():
  print("Hello from a function")

my_function()
print("_____________________")


# function with argument
def my_function1(fname):
  print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")
print("_____________________")

# function with number of argument
def my_function2(fname, lname):
  print(fname + " " + lname)

my_function2("Emil", "Refsnes")
print("_____________________")

#If you do not know how many arguments that will be passed into your function,
# #add a * before the parameter name in the function definition.
def my_function3(*kids):
  print("The youngest child is " + kids[2])

my_function3("Emil", "Tobias", "Linus")
print("_____________________")

#You can also send arguments with the key = value syntax.

def my_function4(child3, child2, child1):
  print("The youngest child is " + child3)

my_function4(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
print("_____________________")
#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function5(**kid):
  print("His last name is " + kid["lname"])

my_function5(fname = "Tobias", lname = "Refsnes")
print("_____________________")

# default parameter
def my_function6(country = "Norway"):
  print("I am from " + country)

my_function6("Sweden")
my_function6("India")
my_function6()
my_function6("Brazil")
print("_________________________________")


# passing a list as an argument
def my_function7(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function7(fruits)
print("_________________________")

# return value
def my_function8(x):
  return 5 * x

print(my_function8(3))
print(my_function8(5))
print(my_function8(9))
print("_________________________")

# recurtion function: means function call inside function itself
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

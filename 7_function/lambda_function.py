# lambda or anonymous function.
# The function is called with a lambda function and 
# an iterable and a new reduced result is returned.

#program 1:
                                  # declaration of lambda
square= lambda x:x*x
                                    # calling of lambda
result=square(4)
print("Square: ",result)


# program 2: using lambda executed expression
b = lambda a: a + 10
print("SUM: ",b(5))

# program 3: multiple argument using lambda
x = lambda a, b ,c: a * b * c
print("MULTIPLICATION: ",x(5, 6,5))


# more than two argument
x = lambda a, b, c : a + b + c
print("SUM: ",x(5, 6, 2))


# Use that function definition to make a function 
# that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n

mul = myfunc(int(input("Enter number")))

print("ANS: ",mul(int(input("Enter number"))))

# 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter(lambda x: x % 2 == 0, list1)
print(list(filter(lambda x: x % 2 == 0, list1)))
# operator : special character which can perform a specific task
# ex +, -,* < > ?

# 1. Arithmetic: which can perform a mathematical functions  (+, - ,* ,/ ,%(modulus) (its gives us a reminder),
# **( exponent (power), //(floor division)( discard after point value)

a=int(input("enter no"))
b=int(input("enter no"))
c=a+b
print(f"a+b: {c}")
c=a-b
print(f"a-b: {c}")
c=a*b
print(f"a*b: {c}")
c=a/b  # division and gives quotation
print(f"a/b: {c}")
c=a%b # its a modulus and provide reminder
print(f"a%b: {c}")
c=a**b  # power operator
print(f"a**b: {c}")
c=a**4
print(f"a**4: {c}")
c=a//b
# casting means datatype conversion ..
# int /int  gives floating but when we don't want point value then use floor division

print(f"a//b: {c}")

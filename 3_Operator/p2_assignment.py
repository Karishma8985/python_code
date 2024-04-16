# operator : special character which can perform a specific task
# ex +, -,* < > ?

# 1. Assignment: Assign value to variable  (=,+=, -=,*=,/= ,%=(modulus) (its gives us a reminder),
# **=( exponent (power), //=(floor division)( discard after point value)
# its a short hand of arithmetic
# a=b  ( b's values pass to the a)
# a+-=b   a+b is store in a

a=int(input("enter no"))
b=int(input("enter no"))
a+=b
print(f"a+b: {a}")
a-=b
print(f"a-b: {a}")
a*=b
print(f"a*b: {a}")
a/=b  # division and gives quotation
print(f"a/b: {a}")
a%=b # its a modulus and provide reminder
print(f"a%b: {a}")
a**=b  # power operator
print(f"a**b: {a}")
a**=4
print(f"a**4: {a}")
a//=b
# casting means datatype conversion ..
# int /int  gives floating but when we don't want point value then use floor division

print(f"a//b: {a}")

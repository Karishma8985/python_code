# logical operator: it works on two or more conditions (a==b)
# ans is in true / false  ( operator : and , or , not)

# 1. and: when all conditions are true then your answer is true
a = int(input("enter no"))
b = int(input("enter no"))
c = int(input("enter no"))

d = a < b and b < c
print(f"a<b and b<c: {d}")

# 2. or: at least one condition should be true then your ans is true

d = a < b or b < c
print(f"a<b or b<c: {d}")

# 3. not: it's an unary operator ... flip the answer
#  ture -> false ///// false-> true
d = not(a < b and b < c)
print(f"not(a<b and b<c): {d}")
d=not(a==5)
print(f"not(a==5) : {d}")


# if elif else : when we have possibility of answers are 3.  else does not contain any condition

n = int(input("enter no: "))
if ( n > 0):
    print(f" {n} is positive no")
elif(n==0):
    print(f" {n} is zero no")
else:
    print(f" {n} is negative no")


# program for finding profit or loss for product. sp(selling price)/cp(cost price)
sp= int(input("Enter selling price"))
cp= int(input("Enter cost price"))

if (sp>cp):
    profit=sp-cp
    print (f" Profited in product is {profit}.")
elif (sp<cp):
    loss= cp-sp
    print(f"there is loss in product is {loss}")
else:
    print(f"there is no profit and loss.")

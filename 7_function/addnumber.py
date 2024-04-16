def addnumber(n1,n2):               # function declaration    
    add=n1+n2                   
    print("Addition: ",add)
    
def subnumber(n1,n2):
    sub=n1-n2
    print("Subtraction: ",sub)
    
num1=int(input("Enter number"))
num2=int(input("Enter another number"))
addnumber(num1,num2)                        # function calling
subnumber(num1,num2)
ch=input("enter your choice..(+,-,*,/,%,**,//)")
a=int(input("enter no"))
b=int(input("enter no"))
match(ch):
    case '+':
        print(f" a+b: {a+b}")

    case '-':
        print(f" a+b: {a-b}")
     
    case '*':
        print(f" a+b: {a*b}")
        
    case '/':
        print(f" a+b: {a/b}")
        
    case '%':
        print(f" a+b: {a%b}")
        
    case '**':
        print(f" a+b: {a**b}")
        
    case '//':
        print(f" a+b: {a//b}")
    
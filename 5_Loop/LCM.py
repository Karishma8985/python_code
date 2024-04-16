a=int(input("enter no"))
b=int(input("enter no"))
max = a if(a>b) else b
while(1):
    if(max%a==0 and max%b==0):
        print(f" LCM  is {max}")
        break
    max+=1
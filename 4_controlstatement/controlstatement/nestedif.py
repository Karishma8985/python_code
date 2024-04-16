# nested if else  : if inside another if ,
# finding greatest no.

a = int(input("enter no"))
b = int(input("enter no"))
c = int(input("enter no"))
d = int(input("enter no"))

if ( a > b):
    if( a > c):
        if(a > d):
            print(f"{a} is big")
        else:
            print(f"{d} is big")
    else:
        if (c > d):
            print(f"{c} is big")
        else:
            print(f"{d} is big")
else:
    if (b > c):
        if (b> d):
            print(f"{b} is big")
        else:
            print(f"{d} is big")
    else:
        if (c > d):
            print(f"{c} is big")
        else:
            print(f"{d} is big")




# program for leap year
# votting eligibility  1 check nationlity and then age
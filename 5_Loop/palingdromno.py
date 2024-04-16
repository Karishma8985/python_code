n=int(input("Enter any number:"))
org=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
    
if(org==rev):
    print(f"The {org}  is palindrome  number")
else:
    print(f"The {org}  is Not a palindrome!")
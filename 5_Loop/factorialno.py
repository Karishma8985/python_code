# program for finding factorial no
n=int(input("enter no"))
fact=1
for i in range(1,n+1):
    fact*=i
print(f"factorial of {n} is {fact}")
print()
print('-'*30) 
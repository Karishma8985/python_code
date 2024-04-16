# Program to check if a number is prime or not
n=int(input("enter no"))
count=0

for i in range(1, n+1):
        if (n % i) == 0:
            count+=1
            
if (count==2):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
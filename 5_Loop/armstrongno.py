# armstrong no are 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748

n = int(input("Enter a number: "))
count=0
sum = 0
org= n

while(n!=0):
    count+=1
    n//=10
    
print(f"count: {count}")
n=org
while (n != 0):
   rem = n % 10
   sum += rem ** count
   n //= 10

# display the result
if (org == sum):
   print(org,"is an Armstrong number")
else:
   print(org,"is not an Armstrong number")
   
   
   
# series of armstrong no
# Program to check Armstrong numbers in a certain interval

start = int(input("enter start no"))
end = int(input("enter end no"))

for n in range(start, end + 1):
    length = len(str(n))
    sum = 0
    rev=0
    org = n
    while org > 0:  # bcoz here n is string
       rem = org % 10
       sum += rem ** length
       org //= 10

    if (n == sum):
       print(n,end="  ")

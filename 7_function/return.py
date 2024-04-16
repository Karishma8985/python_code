# using function find absolute value of number
def get_absolute(num):
    if num>=0:
        return num
    else:
        return -num

n=int(input("Enter positive or negative number:  "))

print(get_absolute(n))
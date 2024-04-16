# string == group of characters
# alphabets,number,special char(symbol)
# you have to use '' or ""

name='jay'
# title() = first letter is convert in capital letter
print(f"name: {name}")

#print(f"constant {var}")

print(f"name: {name.title()}")

# f means formate string , variable as well as constant write together
# name= input("enter name")
# print(f"name: {name}")
# print(f"name: {name.title()}") 

# upper()= all letters converted in upeer case
print(f"name: {name.upper()}")

#lower()= all letters converted in small case
print(f"name : {name.lower()}")

print(f"name: {name.capitalize()}")

# rstrip()= remove extra space 
print(name.rstrip())

#string slice operator variable[start:end:gap]
var = "i like python programming"
print(var[:])
print(var[0:7])
print(var[0:])
print(var[:13])
print(var[0:10:2])
print(var[5:17:3])

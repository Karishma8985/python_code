# List
person={'firstname':'Nikhil','lastname':'Sharma','age':'25','city':'Ahmedabad'}
print(person)

per=person['firstname'].title()
per1=person['lastname'].title()
per2=person['city'].title()
per3=person['age'].title()

print(f"First name is {per}.")
print(f"Last name is {per1}.")
print(f"His age is {per3}.")
print(f"He lives in {per2}.")

for key, value in person.items():
    print(value.title())


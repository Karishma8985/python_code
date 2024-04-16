# favourite number

person={'Rita':6,'Nakul':4,'Isha':9,'Trupti':2,'Mihika':3}
favourite_number=person['Rita']
favourite_number1=person['Nakul']
favourite_number2=person['Isha']
favourite_number3=person['Trupti']
favourite_number4=person['Mihika']

print(f"favourite number of Rita is: ",favourite_number)
print(f"favourite number of Nakul is: ",favourite_number1)
print(f"favourite number of Isha is: ",favourite_number2)
print(f"favourite number of Trupti is: ",favourite_number3)
print(f"favourite number  of Mihika is: ",favourite_number4)

for key,value in person.items():

#     print(f"\nKey:{key}")
 #    print(f"\nValue:{value}")

    print(f"\n Name: {key}  Favourite numbar: {value}")
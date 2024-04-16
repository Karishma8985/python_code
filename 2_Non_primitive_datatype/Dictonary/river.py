major_river={'Nile':'Egypt','Ganga':'India','Amazon':'Brazil','Leena':'Russia','Bhrahmputra':'India'}
# print(major_river.keys())
# print(major_river.values())
print(f"\t Major Rivers:")

for river in major_river.keys():
   print(river.title())
print(f"\t Country:")

for country in major_river.values():
   print(country.title())
# print(f"\t Major Rivers :",major_river.keys())

for key,value in major_river.items():
   print(f"\tThe {key} is runs through {value}.")


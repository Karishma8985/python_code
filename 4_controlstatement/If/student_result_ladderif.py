maths=int(input("Enter obtain marks"))
english=int(input("Enter obtain marks"))
hindi=int(input("Enter obtain marks"))
science=int(input("Enter obtain marks"))
computer=int(input("Enter obtain marks"))

print("Obtain marks: ")
print("Maths: ",maths)
print("English: ",english)
print("Hindi: ",hindi)
print("Science: ",science)
print("Computer",computer)

total=maths+english+science+hindi+computer
print("Total : ",total)

per=(total*100)/500
print("Percentage: ",per)
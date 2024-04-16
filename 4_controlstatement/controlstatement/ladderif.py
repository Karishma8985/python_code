# if elif else : when we have possibility of answers are multiple.  else does not contain any condition

#simple program for edding numbers
"""print("Enter the marks in 5 sub.")
python=int(input("enter marks"))
java=int(input("enter marks"))
html=int(input("enter marks"))
c=int(input("enter marks"))
iot=int(input("enter marks"))

sum=python+java+c+iot+html
# avg=sum/5
perc=(sum*100)/500
print(f"total of marks:{sum}")
print(f"percentage marks:{perc}")
if(perc<=100 and perc>=90):
    print(f" Grade O")
elif(perc<90 and perc>=80):
    print(f" Grade A ")
elif(perc<80 and perc>=70):
    print(f" Grade B ")
elif(perc<70 and perc>=50):
    print(f" Grade C")
elif(perc<50 and perc>=40):
    print(f" Grade D")
else:
    print(f" Fail")  """

# program to find Zodiac sign depend on date of birth and birth month
day = int(input ("enter your birth date."))
month =int(input ("enter your birth month."))

if((month==3 and day>=21 and day<=31) or (month==4 and day>=1 and day<=19)): #  Aries (Ram): March 21–April 19
    print(f" your zodiac is Aries")
elif((month==4 and day>=20 and day<=30) or (month==5 and day>=1 and day<=20)): #  Taurus (Bull): April 20–May 20
    print(f" your zodiac is Taurus")

else:
    print("please insert right date and month")
# ♊ Gemini (Twins): May 21–June 21
#
#
#♋ Cancer (Crab): June 22–July 22
#
# ♌ Leo (Lion): July 23–August 22
#
# ♍ Virgo (Virgin): August 23–September 22
#
# ♎ Libra (Balance): September 23–October 23
#
# ♏ Scorpius (Scorpion): October 24–November 21
#
# ♐ Sagittarius (Archer): November 22–December 21
#
# ♑ Capricornus (Goat): December 22–January 19
#
# ♒ Aquarius (Water Bearer): January 20–February 18
#
# ♓ Pisces (Fish): February 19–March 20
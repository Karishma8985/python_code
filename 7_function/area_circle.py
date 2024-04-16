# define function
def areaOfCircle(rad):
    ar = 3.14*rad*rad
    return ar

def color1():
    color_cost=12
    cost=areaOfCircle(r)*color_cost
    print("costing of color: ",cost)
    
# main
r= float(input("Enter the Radius of Circle: "))
#r = float(input())
a = areaOfCircle(r)
print("\nArea = ", a)
color1()
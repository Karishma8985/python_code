# store information about a pizza being ordered.
pizza={'crust':'thick','topping':['mushrooms','extra cheese','onions']}
print(f"You ordered a {pizza['crust']}-crust pizza " "with the following toppings:")
for topping in pizza['topping']:
    print("\t" + topping)
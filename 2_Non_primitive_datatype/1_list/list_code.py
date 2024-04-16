# list means collection of  different kinds of data type , changeble, idexed, ordered...
# denoted in square braket []

fruits = ['banana','apple','grapes']
# list = [ 0,1,2] indexed
print(fruits)

# membership operator (in)
for fruit in fruits:
    print(fruit.title())
print('-'*20)    
# indexed , by default index start from 0
print(f"1st indexed element: {fruits[1].title()}")

# changeble:  inserted values can be changed

fruits[0]='guava'
print(fruits)   #['guava', 'apple', 'grapes']
print('-'*30) #------------------------------
# manupulating of list ( change)
# append(val) : element add to the end
fruits.append('banana')
print(fruits)           #['guava', 'apple', 'grapes', 'banana']

# insert(position,val)
fruits.insert(1,'papaya')
print(fruits)           #['guava', 'papaya' ,'apple', 'grapes', 'banana']

message = f"i love {fruits[3].title()}"
print(f"message: {message}")
# negative index
#list[-1]  == last value
print(fruits[-1])

# to delete value
del fruits[1]
print(fruits)


# pop is also used for deleting value but it sored and can used in another time
fruits = ['banana','apple','grapes','papaya','guava','orange']
poped_ele= fruits.pop()
print(f"poped element is : {poped_ele}")
print(fruits)

# pop by index
poped = fruits.pop(1)
print(f"poped : {poped}")

#remove elements
fruits.remove('grapes')
print(fruits)

# length of string
x=len(fruits)
fruits = ['banana','apple','grapes','papaya','guava','orange']
# organizing list
# assending order
fruits.sort()
print(fruits)

# descending order
fruits.sort(reverse=True)
print(fruits)
print("___________________")
# temparory sort
print(fruits)
print(sorted(fruits))

print(fruits)

# reverse print

fruits.reverse()
print(fruits)
print("___________________")





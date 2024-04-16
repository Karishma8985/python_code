fruits=[]
fruits.append('banana')
fruits.append('apple')
fruits.append('orange')
fruits.append('papaya')
print(fruits)

# for removing or deleteing values from list
# del= delete value
# pop == remove from last ,or can remove from index
# diff bet del, pop : u can't store del value ///// poped value u can store and use in your code

del fruits[1] 
print(fruits)

poped_ele= fruits.pop()
print(f"poped element is : {poped_ele}")


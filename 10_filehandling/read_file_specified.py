# read file for specified contain.
# var1= open("file name",'mode')
file=open("text2.txt",'r')
str=file.read(10)
# var = var1.read(contain number)
print("Read string is: ",str)
file.close()
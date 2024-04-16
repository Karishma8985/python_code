file = open("text.txt", "r")
str = file.read(10)
print("Read String is : ", str)

# Check current position
position = file.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = file.seek(0, 0)
str = file.read(10)
print("Again read String is : ", str)
# Close opend file
file.close()

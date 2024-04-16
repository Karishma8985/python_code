for i in range(0, 5):
    num = 1
    for j in range(0, i+1):
        print(num, end=" ")
        num = num + 1
    print()
last_num = 6
for row in range(1, last_num):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")
value = 65
for i in range(0, 5):
    for j in range(0, i+1):
        ch = chr(value)
        print(ch, end=" ")
        value = value + 1
    print()
n = 5
alph = 65
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print(chr(alph), end=" ")
		alph += 1
	alph = 65
	print()
h = eval(input("Enter diamond's height: "))

for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))
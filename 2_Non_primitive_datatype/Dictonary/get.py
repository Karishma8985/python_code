# using get() to access values

alien={'color':'green','speed':'slow'}
# print(alien['point'])
pointvalue=alien.get('point','no point value assigned.')
print(pointvalue)
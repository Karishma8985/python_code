# syntax of dictionary
# dictionary means collection of multiple datatype but access by keys and their values...
# here index is replace by keys
# key must be unique
# dict = {'key':'value'}

alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0['speed'])
print(alien_0)

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['color_ch']= 'yellow'
print((alien_0))

del alien_0['points']
print(alien_0)

# use of get function
point_value = alien_0.get('points', 10)
print(point_value)
print(alien_0)


alien={'color':'green','point':5}
print(alien['color'])
print(alien['point'])
print(alien)

newpoint=alien['point']+1
print(f"You just earned {newpoint} point!")

alien['x_position']=0
alien['y_position']=25
print(alien)
print('____________________________')

alien={}
alien['color']='green'
alien['point']=5
print(alien)

# modifying value in a dictionary

alien={'color':'green'}
print(f"The alien is {alien['color']}.")

# modifing value
alien={'color':'yellow'}
print(f"The alien is now {alien['color']}.")

# track position

alien={'x_position':0,'y_position':25,'speed':'medium'}
print(f"original position:{alien['x_position']}")

# move the alien to the right.
# determine how far to move the alien based on ots current speed.

if alien['speed']=='slow':
    x_increment=1
elif alien['speed']=='medium':
    x_increment=2
else:
    # this must be a fast alein.
    x_increment=3

# new position is the old position increment
alien['x_position']=alien['x_position']+x_increment

print(f"new position:{alien['x_position']}")


# dictionary of similar objects/storing data


favourite_language={'jen':'python', 'sarah':'c', 'edward':'ruby', 'phil':'python'}

language=favourite_language['sarah'].title()

print(f"sarah's favourite language is {language}.")







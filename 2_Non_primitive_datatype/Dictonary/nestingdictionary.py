alien0={'color':'green','points':5}
alien1={'color':'yellow','points':10}
alien2={'color':'red','points':15}

aliens=[alien0,alien1,alien2]

for alien in aliens:
    print(alien)
# make an empty list for storing aliens
aliens=[]

            # make 30 green aliens.
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color']=='green':
       alien['color']='yellow'
       alien['speed']='medium'
       alien['points']=10

    elif alien['color']=='yellow':
      alien['color']='red'
      alien['speed']='fast'
      alien['points']=15

    # shoe how many aliens u created.
print(f"Total number of aliens:{len(aliens)}")

    # slow the first 5 aliens.
for alien in aliens[:5]:
    print(alien)



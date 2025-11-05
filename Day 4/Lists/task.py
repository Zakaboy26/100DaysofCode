#Lists eg: fruits [item1, item2] can be mixed data types

america_states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#These are all in the order in which they joined the union^ so if we:
print(america_states[0]) #It will print Delaware the first one, if -1 is the index...
#...then u get the last item

#If you want to change an item in a list:
america_states[1] = 'Pencil Vania'

#To add to the list
america_states.append("ShanstarLand")

#You can also add using extend, which adds a bunch of items/a list
america_states.extend(["ZeeLand","VMLand"])

#You can also remove using, remove lol..
#By name:
america_states.remove('New Jersey')
#By index:
america_states.pop(0)

print(america_states)#It will show Pencil Vania and ShanstarLand + removed NJ and Delaware

#READ DOCUMENTATION THERES MORE METHODS BUT U DONT NEED TO MEMORISE
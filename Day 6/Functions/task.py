#defining our function
def zaka_function():
    print("Hello")
    print("And bye.")

#To call a function
zaka_function()

###REEBORGS CHALLENGE HURDLE####
'''def turn_right():
    turn_left()
    turn_left()
    turn_left()


def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

###FOR LOOP EXAMPLE###
for i in range(0, 6):
    hurdle()

###WHILE LOOP EXAMPLE###
no_of_hurdles = 6
while no_of_hurdles > 0:
    hurdle()
    no_of_hurdles -= 1 '''

###HURDLE 2 WITH MOVING VARIABLE FINISH LINE###
'''def turn_right():
    turn_left()
    turn_left()
    turn_left()


def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


at_goal() == False
while at_goal() == False:
    hurdle()    '''

###HURDLE 3 WITH VARIABLE BARRIERS###
'''def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    if front_is_clear():
        move()
    else:
        jump()
        '''

###HURDLE 4 WITH VARIABLE WALL HEIGHTS AND POS###
'''def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    move()
    while wall_in_front() != True:
        move()
    turn_left()

while at_goal() != True:
    if front_is_clear():
        move()
    else:
        jump()
        
    
    '''

####MAZE###
'''def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()'''
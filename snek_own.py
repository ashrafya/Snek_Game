import pygame, sys, time, random
from pygame.locals import *

pygame.init()
global number
global frame
global board_size
global cycle_allownace
cycle_allownace = 1.4
board_size = 10
frame = 0
number = 0

fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Snek_api_yawar_elsa")  #setting the caption for the game
outberry = 0
outberrydir = 'right'

redColour = pygame.Color(255, 0, 0)  #making red colour
greenColor =(0,255,0)
blackColour = pygame.Color(0, 0, 0)     #making black colour
whiteColour = pygame.Color(255, 255, 255)       #making white colour
anyColor = pygame.Color(15,153,242) 
greyColour = pygame.Color(150, 150, 150)        #making grey colour
snakePosition = [100, 100]          #snake starts to move at the 100,100 coordinate
snakeSegments = [[100, 100]] # the snake starts off with being two blocks long, each block is 20 by 20 in size
raspberryPosition = [100, 100] #the starting position of the raspberry
raspberrySpawned = 1  #the number of raspberies spawned, initially
direction = 'down'       #The starting direction the snake starts to move in


# changeDirection is for what will next direction snake and to take
changeDirection = direction
# global flag is use when raspberry is in wrong side and snake have to turn to go in specific location
global flag
global count
count=0
flag = True # when flag is true it continues in the same direction

# dirout variable is uses when raspberry position is in wrong side and snake must turn
# to go in checkdir output location and ignoring direction results  whatinput() function
dirout = 'down'  #Dunno what this means


# when snake crash function called
def gameOver():
    global number
    global count
    number+=1

    f = open("scores_1.4.csv", "a+")
    f.write('{}\n'.format(count))
    f.close()
    f = open("scores_1.4.csv", "r")
    #(f.read())
    
    gameOverFont = pygame.font.Font('freesansbold.ttf', 20)  # the font is the first argument, and second argument is the font size
    gameOverSurf = gameOverFont.render('score is {} {}' .format(count, len(snakeSegments)), True, whiteColour) ##s irst argument when game ends, true needed to # it, and which colour
    gameOverRect = gameOverSurf.get_rect() #creates a rectangular object for the text
    gameOverRect.midtop = (80, 100) ##s in the midtop of the rectangle object made at the (x,y) coordinates
    playSurface.blit(gameOverSurf, gameOverRect) #blit take in the layout of teh surface and the rectangle to type in , and then draws it
    pygame.display.flip() #updates the entire screen display
    # #(len(snakeSegments))
    # #(count)
    #time.sleep(2)  #pauses the execution of the following command for (n) seconds
    pygame.quit() #deactivates the pygame library
    sys.exit() #exit the system of python

#fix checkdir function, cuz end wall cases seem a bit fishy
# function called when raspberry position out of accessible location by whatinput() function
def checkdir():
    global flag
    global dirout
    # make fxn upto 4 blocks for a,s,w,d
    a = [snakePosition[0]-20, snakePosition[1]]
    a2 = [snakePosition[0]-40, snakePosition[1]]
    a3 = [snakePosition[0]-60, snakePosition[1]]
    a4 = [snakePosition[0]-80, snakePosition[1]]
    w = [snakePosition[0], snakePosition[1]-20]
    w2 = [snakePosition[0], snakePosition[1]-40]
    w3 = [snakePosition[0], snakePosition[1]-60]
    w4 = [snakePosition[0], snakePosition[1]-80]
    d = [snakePosition[0]+20, snakePosition[1]]
    d2 = [snakePosition[0]+40, snakePosition[1]]
    d3 = [snakePosition[0]+60, snakePosition[1]]
    d4 = [snakePosition[0]+80, snakePosition[1]]
    s = [snakePosition[0], snakePosition[1]+20]
    s2 = [snakePosition[0], snakePosition[1]+40]
    s3 = [snakePosition[0], snakePosition[1]+60]
    s4 = [snakePosition[0], snakePosition[1]+80]
    if changeDirection == 'right':  #if direction is changed to right
        if snakePosition[0] > raspberryPosition[0]: # and if the snake x coor is ahead of raspberry x coor
            #("in checkdir if right") 
            y = [snakePosition[0], snakePosition[1]+20]
            # into self
            flag = False
            if y[1]<=180 and s not in snakeSegments:
                dirout = 'down'
            elif w not in snakeSegments:
                if w[1]>=0:
                    dirout = 'up'
            else:
                dirout = 'right'
            #("log in checkdir :" + dirout)  # then essentiall change the direction to down
        if snakePosition[0] < raspberryPosition[0]:
            if d in snakeSegments and w in snakeSegments:
                dirout = 'down'
            elif d in snakeSegments and s in snakeSegments:
                dirout = 'up'
            elif d in snakeSegments:
                if s not in snakeSegments and s2 not in snakeSegments and s3 not in snakeSegments:
                    dirout = 'down'
                elif w not in snakeSegments and w2 not in snakeSegments and w3 not in snakeSegments:
                    dirout = 'up'


    if changeDirection == 'left':   #if change direction is left
        if snakePosition[0] < raspberryPosition[0]:   # and snake position is more to the left than the raspbberry
            y = [snakePosition[0], snakePosition[1]-20]
            #("in checkdir if left")
            #into self
            flag = False
            if y[1]>=0 and w not in snakeSegments:
                dirout = 'up'  
            elif s not in snakeSegments:
                if s[1] <=180:
                    dirout = 'down'
            else:
                dirout = 'left'
            #("log in checkdir :" + dirout) 
        if snakePosition[0] > raspberryPosition[0]:
            if a in snakeSegments and w in snakeSegments:
                dirout = 'down'
            elif a in snakeSegments and s in snakeSegments:
                dirout = 'up'
            elif a in snakeSegments:
                if s not in snakeSegments and s2 not in snakeSegments and s3 not in snakeSegments:
                    dirout = 'down'
                elif w not in snakeSegments and w2 not in snakeSegments and w3 not in snakeSegments:
                    dirout = 'up'
                


    if changeDirection == 'up':   # if direction is up
        if snakePosition[1] < raspberryPosition[1]:  # and teh snake is position higher than the new raspberry
                                                     # add clause that snake should bump into wall
            y = [snakePosition[0]+20,snakePosition[1]]
            #("in cheakdir if up")
            flag = False
            #into self 
            if y[0] <=180 and d not in snakeSegments:
                dirout = 'right'   # the new direction i sturned to right
            elif a not in snakeSegments:
                if a[0] >=0:
                    dirout = 'left'
            else:
                dirout = 'up'
            #("log in checkdir :" + dirout)
        if snakePosition[1] < raspberryPosition[1]:
            if w in snakeSegments and d in snakeSegments:
                dirout  = 'left'
            elif w in snakeSegments and a in snakeSegments:
                dirout = 'right'
            elif w in snakeSegments:
                if a not in snakeSegments and a2 not in snakeSegments and a3 not in snakeSegments:
                    dirout = 'left'
                elif d not in snakeSegments and d2 not in snakeSegments and d3 not in snakeSegments:
                    dirout = 'right' 
            
    ##(snakeSegments)
    if changeDirection == 'down':    # if the direction is down
        if snakePosition[1] > raspberryPosition[1]: # and teh snake is below the actual 
            #("in cheackdir if down")
            flag = False
            y = [snakePosition[0]-20,snakePosition[1]]
            #into self
            if y[0]>=0 and a not in snakeSegments: #and statement here to make sure snake doesnt hit itself
                dirout = 'left'   # the direction that goes out is False
            elif d not in snakeSegments:
                if d[0] <=180:
                    dirout = 'right'
            else:
                dirout = 'down'
            #("log in checkdir :" + dirout)  
        if snakePosition[1] < raspberryPosition[1]:
            if s in snakeSegments and d in snakeSegments:
                dirout = 'left'
            elif s in snakeSegments and a in snakeSegments:
                dirout = 'right'
            elif s in snakeSegments:
                if a not in snakeSegments and a2 not in snakeSegments and a3 not in snakeSegments:
                    dirout = 'left'
                elif d not in snakeSegments and d2 not in snakeSegments and d3 not in snakeSegments:
                    dirout = 'right'


def whatinput():   # makes decision about the next direction. need to add condition that it doesnt into itself here
    a = [snakePosition[0]-20, snakePosition[1]]
    a2 = [snakePosition[0]-40, snakePosition[1]]
    a3 = [snakePosition[0]-60, snakePosition[1]]
    a4 = [snakePosition[0]-80, snakePosition[1]]
    w = [snakePosition[0], snakePosition[1]-20]
    w2 = [snakePosition[0], snakePosition[1]-40]
    w3 = [snakePosition[0], snakePosition[1]-60]
    w4 = [snakePosition[0], snakePosition[1]-80]
    d = [snakePosition[0]+20, snakePosition[1]]
    d2 = [snakePosition[0]+40, snakePosition[1]]
    d3 = [snakePosition[0]+60, snakePosition[1]]
    d4 = [snakePosition[0]+80, snakePosition[1]]
    s = [snakePosition[0], snakePosition[1]+20]
    s2 = [snakePosition[0], snakePosition[1]+40]
    s3 = [snakePosition[0], snakePosition[1]+60]
    s4 = [snakePosition[0], snakePosition[1]+80]
    if direction == 'right':        #if snake is moving right

        #coochie problem
        if d2 in snakeSegments:
            if [snakePosition[0]-20, snakePosition[1]-20] in snakeSegments:
                if [snakePosition[0]-20, snakePosition[1]+20] in snakeSegments:
                    if s not in snakeSegments and s2 not in snakeSegments and s3 not in snakeSegments:
                        return 'down'
                    elif w not in snakeSegments and w2 not in snakeSegments and w3 not in snakeSegments:
                        return 'up'
                    elif w not in snakeSegments and w2 not in snakeSegments:
                        return 'up'
                    elif s not in snakeSegments and s2 not in snakeSegments:
                        return 'down'
                    elif w in snakeSegments:
                        return 'down'
                    elif s in snakeSegments:
                        return 'up'
        if snakePosition[0] == raspberryPosition[0]:  # if snake and raspberry in the same column
            #self forward
            if d in snakeSegments:
                #('this')
                if snakePosition[1] < raspberryPosition[1] and s in snakeSegments:  # if snake is above raspberry then go down
                    return 'up'
                elif snakePosition[1] > raspberryPosition[1] and w in snakeSegments:                           #else if the snake is below the raspberry then go up
                    return 'down'
                if s not in snakeSegments and s2 not in snakeSegments and s3 not in snakeSegments:
                    return 'down'
                elif w not in snakeSegments and w2 not in snakeSegments and w3 not in snakeSegments:
                    return 'up'
                elif w not in snakeSegments and w2 not in snakeSegments:
                    return 'up'
                elif s not in snakeSegments and s2 not in snakeSegments:
                    return 'down'
                if s not in snakeSegments:
                    return 'down'
                elif w not in snakeSegments:
                    return 'up'

            #('that')
            if snakePosition[1] < raspberryPosition[1] and s not in snakeSegments:  # if snake is above raspberry then go down
                return 'down'
            elif snakePosition[1] > raspberryPosition[1] and w not in snakeSegments:                           #else if the snake is below the raspberry then go up
                return 'up'
            else:
                return 'right'
        if d in snakeSegments:
            if snakePosition[1] < raspberryPosition[1] and s in snakeSegments:  # if snake is above raspberry then go down
                return 'up'
            elif snakePosition[1] > raspberryPosition[1] and w in snakeSegments:                           #else if the snake is below the raspberry then go up
                return 'down'
            if w in snakeSegments:
                return 'down'
            elif s in snakeSegments:
                return 'up'
            elif s not in snakeSegments and s2 not in snakeSegments and s3 not in snakeSegments:
                return 'down'
            elif w not in snakeSegments and w2 not in snakeSegments and w3 not in snakeSegments:
                return 'up'
            elif w not in snakeSegments and w2 not in snakeSegments:
                return 'up'
            elif s not in snakeSegments and s2 not in snakeSegments:
                return 'down'
            else:
                return 'right'
            

        else:
            return 'right'  # if snake in not the same column then keep going right (could add the new fxn here too)
    
    if direction == 'left':  # if snak eis going left
        if a2 in snakeSegments:
            if [snakePosition[0]+20, snakePosition[1]-20] in snakeSegments:
                if [snakePosition[0]+20, snakePosition[1]+20] in snakeSegments:
                    if s not in snakeSegments and s2 not in snakeSegments and s3 not in snakeSegments:
                        return 'down'
                    elif w not in snakeSegments and w2 not in snakeSegments and w3 not in snakeSegments:
                        return 'up'
                    elif w not in snakeSegments and w2 not in snakeSegments:
                        return 'up'
                    elif s not in snakeSegments and s2 not in snakeSegments:
                        return 'down'
                    elif w in snakeSegments:
                        return 'down'
                    elif s in snakeSegments:
                        return 'up'

        if snakePosition[0] == raspberryPosition[0]:  # if the snake is in the same column as teh raspberry
            #self forward
            if a in snakeSegments:
                #('this')
                if snakePosition[1] < raspberryPosition[1] and s in snakeSegments:  # if snake is above teh raspberry, go down
                    return 'up'
                elif snakePosition[1] > raspberryPosition[1] and w in snakeSegments:           #else the snake goes up
                    return 'down'
                if s not in snakeSegments and s2 not in snakeSegments and s3 not in snakeSegments:
                    return 'down'
                elif w not in snakeSegments and w2 not in snakeSegments and w3 not in snakeSegments:
                    return 'up'
                elif w not in snakeSegments and w2 not in snakeSegments:
                    return 'up'
                elif s not in snakeSegments and s2 not in snakeSegments:
                    return 'down'
                elif s not in snakeSegments: #x
                    return 'down'
                elif w not in snakeSegments:  #y
                    return 'up'


            #('that')
            if snakePosition[1] < raspberryPosition[1] and s not in snakeSegments:  # if snake is above teh raspberry, go down
                return 'down'
            elif snakePosition[1] > raspberryPosition[1] and w not in snakeSegments:           #else the snake goes up
                return 'up'
            else:
                return 'left'
        if a in snakeSegments:
            if snakePosition[1] < raspberryPosition[1] and s in snakeSegments:  # if snake is above teh raspberry, go down
                return 'up'
            elif snakePosition[1] > raspberryPosition[1] and w in snakeSegments:           #else the snake goes up
                return 'down'
            if w in snakeSegments:
                return 'down'
            elif s in snakeSegments:
                return 'up'
            elif s not in snakeSegments and s2 not in snakeSegments and s3 not in snakeSegments:
                return 'down'
            elif w not in snakeSegments and w2 not in snakeSegments and w3 not in snakeSegments:
                return 'up'
            elif w not in snakeSegments and w2 not in snakeSegments:
                return 'up'
            elif s not in snakeSegments and s2 not in snakeSegments:
                return 'down'
            else:
                return 'left'
            
            
        else:
            return 'left'  # if the snake is not in the same column, then it keeps going straight
    
    if direction == 'up':  
        if w2 in snakeSegments:                            #avoiding coochie problem
            if [snakePosition[0]+20, snakePosition[1]-20] in snakeSegments:
                if [snakePosition[0]-20, snakePosition[1]-20] in snakeSegments:
                    if a not in snakeSegments and a2 not in snakeSegments and a3 not in snakeSegments:
                        return 'left'
                    elif d not in snakeSegments and d2 not in snakeSegments and d3 not in snakeSegments:
                        return 'right'
                    elif d not in snakeSegments and d2 not in snakeSegments:
                        return 'right'
                    elif a not in snakeSegments and a2 not in snakeSegments:
                        return 'left'
                    if d not in snakeSegments:
                        return 'right'
                    elif a not in snakeSegments:
                        return 'left'

        if snakePosition[1] == raspberryPosition[1]: # if snake in the same row as the raspberry
            #self forward 
            #a = [snakePosition[0], snakePosition[1]-20]
            if w in snakeSegments:
                #('this')
                if snakePosition[0] < raspberryPosition[0] and d in snakeSegments: # if raspberry is to the right of teh snake, snake moves rigth
                    return 'left'
                elif snakePosition[0] > raspberryPosition[0] and a in snakeSegments:               #if raspberry is to the left of teh snake, then the snake moves to the left
                    return 'right'
                if a not in snakeSegments and a2 not in snakeSegments and a3 not in snakeSegments:
                    return 'left'
                elif d not in snakeSegments and d2 not in snakeSegments and d3 not in snakeSegments:
                    return 'right'
                elif d not in snakeSegments and d2 not in snakeSegments:
                    return 'right'
                elif a not in snakeSegments and a2 not in snakeSegments:
                    return 'left'
                if d not in snakeSegments:
                    return 'right'
                elif a not in snakeSegments:
                    return 'left'

            #('that')
            if snakePosition[0] < raspberryPosition[0] and d not in snakeSegments: # if raspberry is to the right of teh snake, snake moves rigth
                return 'right'
            elif snakePosition[0]>raspberryPosition[0] and a not in snakeSegments:               #if raspberry is to the left of teh snake, then the snake moves to the left
                return 'left'
            else:
                return 'up'
        if w in snakeSegments:
            if snakePosition[0] < raspberryPosition[0] and d in snakeSegments: # if raspberry is to the right of teh snake, snake moves rigth
                return 'left'
            elif snakePosition[0] > raspberryPosition[0] and a in snakeSegments:               #if raspberry is to the left of teh snake, then the snake moves to the left
                return 'right'
            if d in snakeSegments:
                return 'left'
            elif a in snakeSegments:
                return 'right'
            elif a not in snakeSegments and a2 not in snakeSegments and a3 not in snakeSegments:
                return 'left'
            elif d not in snakeSegments and d2 not in snakeSegments and d3 not in snakeSegments:
                return 'right'
            elif d not in snakeSegments and d2 not in snakeSegments:
                return 'right'
            elif a not in snakeSegments and a2 not in snakeSegments:
                return 'left'
            else:
                return 'up'
            
            
            
        else:
            return 'up' # if snake is not in the same row, then it keeps on going up
    
    if direction == 'down':   # snake is going down
        if s2 in snakeSegments:
            if [snakePosition[0]+20, snakePosition[1]+20] in snakeSegments:
                if [snakePosition[0]-20, snakePosition[1]+20] in snakeSegments:
                    if a not in snakeSegments and a2 not in snakeSegments and a3 not in snakeSegments:
                        return 'left'
                    elif d not in snakeSegments and d2 not in snakeSegments and d3 not in snakeSegments:
                        return 'right'
                    elif d not in snakeSegments and d2 not in snakeSegments:
                        return 'right'
                    elif a not in snakeSegments and a2 not in snakeSegments:
                        return 'left'
                    elif d in snakeSegments:
                        return 'left'
                    elif a in snakeSegments:
                        return 'right'



        if snakePosition[1] == raspberryPosition[1]:        #if snake is in the same row as the raspberry
            if s in snakeSegments:
                #('this')
                if snakePosition[0] < raspberryPosition[0] and d not in snakeSegments:
                    return 'right'
                elif snakePosition[0] > raspberryPosition[0] and a not in snakeSegments:
                    return 'left'
                if d in snakeSegments:     
                    return 'left'
                elif a in snakeSegments:  ##### possible change to else, all four directions closed
                    return 'right'
                elif a not in snakeSegments and a2 not in snakeSegments and a3 not in snakeSegments:
                    return 'left'
                elif d not in snakeSegments and d2 not in snakeSegments and d3 not in snakeSegments:
                    return 'right'
                elif d not in snakeSegments and d2 not in snakeSegments:
                    return 'right'
                elif a not in snakeSegments and a2 not in snakeSegments:
                    return 'left'
                if d not in snakeSegments:
                    return 'right'
                elif a not in snakeSegments:
                    return 'left'
                
                
                
            if snakePosition[0] < raspberryPosition[0] and d not in snakeSegments:
                return 'right'
            elif snakePosition[0] > raspberryPosition[0] and a not in snakeSegments:
                return 'left'       
            else:
                return 'down'
        if s in snakeSegments:
            if snakePosition[0] < raspberryPosition[0] and d in snakeSegments:
                return 'left'
            elif snakePosition[0] > raspberryPosition[0] and a in snakeSegments:
                return 'right'
            elif d in snakeSegments:
                return 'left'
            elif a in snakeSegments:
                return 'right'
            elif a not in snakeSegments and a2 not in snakeSegments and a3 not in snakeSegments:
                return 'left'
            elif d not in snakeSegments and d2 not in snakeSegments and d3 not in snakeSegments:
                return 'right'
            elif d not in snakeSegments and d2 not in snakeSegments:
                return 'right'
            elif a not in snakeSegments and a2 not in snakeSegments:
                return 'left'
            else:
                return 'down'
            
        else:
            return 'down'
        '''
        elif snakePosition[1] != raspberryPosition[1]:
            w = [snakePosition[0], snakePosition[1]-20]             #
            a = [snakePosition[0]-20, snakePosition[1]]             #
            s = [snakePosition[0], snakePosition[1]+20]             #
            d = [snakePosition[0]+20, snakePosition[1]]             #
            if s in snakeSegments and a in snakeSegments:
                return 'right'
            elif s in snakeSegments and d in snakeSegments:
                return 'left'
        '''


while True:   #this is the main loop, and only ends when the gameOver() function is called

    # i don't remove the event block that can use to operate snake with keys because some might intrested
    for event in pygame.event.get():   #just checks if the if the 
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = 'left'
            if event.key == K_UP or event.key == ord('w'):
                changeDirection = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))


    # flag initially true for checking snake will have raspberry position accessible or not
    flag = True           
    # this might # the stat of the directon that really help you out to code other thinks that snake never crash :)
    #("current direction :" + changeDirection)  # initially changeDirection is started out as direction (Which was set to down)

    # call checkdir() function to check raspberry position is accessible or not
    checkdir()  #checks if snake is going the right way to the raspberry, if not(changes the direction apprpriately), sets flag to false
                #and changes the output direction 
    changeDirection = dirout  #changeDirection = dirout from checkdir() 
    #change direction is set to the dirout, because changeDirection is implemented in the snake's movement
    #("dirout is : " +dirout)

    #("log checkdir after :" + dirout)


    #checkdir()     #checks if the snake is going in the very opposite direction from the raspberry
    #whatinput()    #checks if the direction is in teh relatively right direction, and changes direction when in the proper row/column
    
    # if flag still true than call second function to do regular things
    if (flag == True):
        changeDirection = whatinput()    #have to change this fxn like checkdir() in case there
                                         # is no change in diretcion, and keeps going straight


        #change direction according to proper row adn column work by whatinput()
        #("log if flag TRUE :" + dirout)
    
    

    # following few lines checking that input is reverse direction to current input than block can not take input
    # issue:if out whatinput() function  continue input of same direction than might snake will crash:(
    #(changeDirection, dirout, direction)


    for event in pygame.event.get():   #just checks if the if the 
        #(event)
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = 'right'
                #('key_r')
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = 'left'
                #("key_l")
            if event.key == K_UP or event.key == ord('w'):
                changeDirection = 'up'
                #('key_u')
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = 'down'
                #('key_d')
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    if changeDirection == 'right' and not direction == 'left': #makes sure snake doesn't reverse on itself
        direction = changeDirection    #changes direction of whatinput() to direction of checkdir()
    if changeDirection == 'left' and not direction == 'right': ##makes sure snake doesn't reverse on itself
        direction = changeDirection
    if changeDirection == 'up' and not direction == 'down': #makes sure snake doesn't reverse on itself
        direction = changeDirection
    if changeDirection == 'down' and not direction == 'up':  #makes sure snake doesn't reverse on itself
        direction = changeDirection
    if direction == 'right': #adds an element that moves to the rigth
        snakePosition[0] += 20                                          #changes the head position
    if direction == 'left': #adds an element that moves to the left
        snakePosition[0] -= 20                                          #changes the head position
    if direction == 'up':   #adds an element that moves to the up
        snakePosition[1] -= 20                                          #changes the head position
    if direction == 'down':  #adds an element that moves to the down
        snakePosition[1] += 20                                          #changes the head position
    #(changeDirection, dirout, direction)

    snakeSegments.insert(0, list(snakePosition))
    frame+=1
    if frame>(((4*board_size)-4)*cycle_allownace):
            gameOver()   
    if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:

        frame=0

        raspberrySpawned = 0   
        harry = random.randrange(0,5)
        #(harry)
        if harry == 0 or harry == 1 or harry == 2:
            count+=60
        elif harry == 3 or harry ==4 or harry == 5:
            count+=20
    else:
        snakeSegments.pop()  # the last elemenet is popped out, i.e. the tail of the snakeSegments

    if raspberrySpawned == 0:   
        x =  random.randrange(0, 9)
        y = random.randrange(0, 9)  
        raspberryPosition = [int(x * 20), int(y * 20)]  
        if raspberryPosition in snakeSegments:
            while raspberryPosition in snakeSegments:
                x = random.randrange(0,9)
                y = random.randrange(0,9)
                raspberryPosition = [int(x*20), int(y*20)]
    if count >2000:
        gameOver()
    print (count)

    
    raspberrySpawned = 1 #now raspberry spawned is 1


    playSurface.fill(blackColour)   #playsurface is filled to balck
    pygame.draw.rect(playSurface, whiteColour, Rect(snakeSegments[0][0], snakeSegments[0][1], 20, 20))
    snakeSegments[0]
    for position in snakeSegments[1:]: #for each element in the snake body list
        pygame.draw.rect(playSurface, anyColor, Rect(position[0], position[1], 20, 20)) #rect takes in arguements (left, top, width, height)
    
    pygame.draw.rect(playSurface, redColour, Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))  #draws the position of the raspberry
    pygame.display.flip()  #refreshes the whole screen, starts again with black, snake, raspberry
    # following code will make gameover when it crash with wall
    if snakePosition[0] >= 200 or snakePosition[0] < 0:  # gamOver() if snake leaves x-axis range
        gameOver()
    if snakePosition[1] >= 200 or snakePosition[1] < 0:  #gameOver() if snake leaves y-axis range
        gameOver()



    
    
    for snakeBody in snakeSegments[1:]:  #starts other than the head of the snake
        if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:#checks if snake head hits any part of the body then gameOver()
            pygame.draw.rect(playSurface, greenColor, Rect(snakeBody[0], snakeBody[1], 20, 20))
            gameOver()
    
    
    fpsClock.tick(20)
    #("\n")
    #(count)


'''
PROBLEMS TO FIX:
1) The raspberry has to be spawned on square where the snake does not exist   #solved
2) Stop the snake bumping into itself                                         #solved
3) improve desion makign of snake when it moves away from berry               #solved
4) The snake hits side wall                                                   #solved
5) giving problem in the four corner cases                                    #solved
6) Making game_board size to 10 by 10                                         #solved
7) moogle = 20, harry = 60                                                    #solved
    - find a way to randomize appearance                                      #solved
    - set different scores                                                    #solved
    - way to add these scores                                                 #solved
8) have to add the total scores to a final file  (do it manually)             #solved 
9) move the snake according to commands (find the code I deleted)             
10) add time constraint to gameOver()
11) wall problem is back                                                      #solved
12) solve the coochie enter problem for trap  ^     for all 4 cases           #solved
                                                >
                                              \/
'''

'''
algorithm to solve problem 3)
- if it is going to hit itself just keep on going straight and try to move the other way next time
- if hit dead end, go the fourth way, i.e. the only way the snake can leave

'''

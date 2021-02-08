from pygame import *

init()
# we only need a screen to get access to the events
# screen line creates a screen we can draw onto
# display.set_mode opens up a game window and sets the window to the size you want it to be
#display.set_mode((width, height))
screen = display.set_mode((640, 480)) # tuple - an array/list that cant be changed
display.set_caption("Graphics") # .set_caption("Text") changes caption on top of the window

endProgram = False

while not endProgram:
    # pygame event loop
    for e in event.get():
        if e.type == QUIT: # this event is called whenever the window is exited
            endProgram = True
    # draw stuff
    # screen.fill((red,green,blue))
    # value for each amount of red/green/blue can go from 0 - 254
    screen.fill((100,100,200)) # fills the screen with a single colour
    # rectangle
    # draw.rect(surface, colour, rectangle, thickness)
    # rectangle is a tuple (X,Y,Width, Height)
    draw.rect(screen, (255,0,0), (10,10,100,100), 4) # outline of rectangle
    # fill rectangle
    # leaving thickness out will make the program assume you want the full colour
    draw.rect(screen, (255,0,0), (200,10,100,100)) # full rectangle
    # circle
    # draw.ellipse(surface, colour, rectangle, thickness)
    # the rectangle is where the circle will be inside of
    draw.ellipse(screen, (0,255,0), (10, 200, 80, 80) , 4)
    # circle
    draw.ellipse(screen, (0,255,0), (200, 200, 80, 80))
    # update the screen
    # display.update() draws all the shapes from memory
    display.update()

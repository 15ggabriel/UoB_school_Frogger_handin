from pygame import *

init()
# we only need a screen to get access to the events!
screen = display.set_mode((640, 480)) # tuple
display.set_caption("Graphics")

# position of ball is stored in x and y
animationTimer = time.Clock()
x = 10
y = 10
endProgram = False

# game loops
# check input
# Update positions / game logic
# draw frame

while not endProgram:
    # Check input
    for e in event.get():
        if e.type == QUIT:
            endProgram = True
        # update position
        x = x + 1 #makes ball move in the x direction
        y = y + 1 # makes ball move in y direction
        # draw stuff
        screen.fill((100,100,200))
        # circle
        draw.ellipse(screen, (0,255,0), (x, y, 40, 40))

        # limit to 30 frames per second
        animationTimer.tick(30)
        # update the screen!
        display.update()
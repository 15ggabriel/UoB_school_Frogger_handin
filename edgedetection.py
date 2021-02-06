from pygame import *

init()
width = 640
height = 480

screen = display.set_mode((width, height)) # tuple
display.set_caption("Graphics")

animationTimer = time.Clock()
x = 10
y = 10
dx = 6  # how fast/direction in x direction (horizontal)
dy = 6  # how fast / direction in y direction (vertical)
endProgram = False

# game loops
# check input
# update positions / gamel logic
# draw frame

while not endProgram:
    # Check input
    for e in event.get():
        if e.type == QUIT:
            endProgram = True
    # update position
    x = x + dx
    y = y + dy
    # border check
    if y < 0 or y > height - 40: # if ball goes off the top or the bottom, it will rebound
        dy = dy * -1 # reverses horizontal direction
    if x < 0 or x > width - 40: # if the ball goes off the left or right side, it will rebound
        dx = dx * -1 # reverses vertical direction
    # draw stuff
    screen.fill((100,100,200))
    # circle
    # the x and y are the coordinates of the top left corner
    # of the rectangle encasing the ball/circle
    draw.ellipse(screen, (0,255,0), (x, y, 40, 40))

    # limit to 30 frames per second
    animationTimer.tick(30)
    # update the screen!
    display.update()

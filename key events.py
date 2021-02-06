from pygame import *

#initialises pygame engine
init()
#we only need a screen to get access to the events
screen = display.set_mode((640, 480))
display.set_caption("The amazing key presser!")

endProgram = False

while not endProgram:
    #pygame event loop
    for e in event.get():
        if e.type == KEYDOWN:
            # K_a represents the A key
            if (e.key == K_a):
                print("A was pressed")
            elif (e.key == K_b): # K_b represents B key
                print("B was pressed")
            elif (e.key == K_ESCAPE): # K_ESCAPE represents escape key
                endProgram = True
            else:
                print("Error: wrong key")
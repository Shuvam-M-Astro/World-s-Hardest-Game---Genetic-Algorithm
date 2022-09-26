from psychopy import core, visual,event
from pyglet.window import key
from gameover import gameover
from movementandcollisionlogic import movementandcollisionlogic
from exit import exit
from levelup import levelup
from end import end
from score import score

import numpy as np

win = visual.Window(size=(640, 480), units="pix",color=(0,0,0),colorSpace='rgb', rgb=(181,100,227))

txt = visual.TextStim(win,text="WHG",pos=(0.0, 200.0), rgb=None, color=(0.1, 0.1, 0.1), colorSpace='rgb')
txt.setAutoDraw(True)


def screen_limits(win):
    """Return screen coordinates left, top, right, bottom"""
    return [
        0 - win.size[0] / 2,
        0 + win.size[1] / 2,
        0 + win.size[0] / 2,
        0 - win.size[1] / 2,
    ]

scr_size = screen_limits(win)

# Checker Stuff
black = [-0.34, -1, -1]
white = [ 1, 1, 1]

# Numpy arrays
tex = np.array([[black, white], [white, black]])
tex = np.tile(tex, (2, 2, 1))


# Numpy arrays
tex2 = np.array([[black, white]])
tex2 = np.tile(tex, (1, 1, 1))

#Draw boundaries with different dimensions
myline1 = visual.Rect(win, width=1, height=200, lineColor="black", fillColor="black", autoDraw=True)
myline2 = visual.Rect(win, width=1, height=100, lineColor="black", fillColor="black", autoDraw=True)
myline3 = visual.Rect(win, width=1, height=50, lineColor="black", fillColor="black", autoDraw=True)
myline4 = visual.Rect(win, width=50, height=1, lineColor="black", fillColor="black", autoDraw=True)
myline5 = visual.Rect(win, width=50, height=1, lineColor="black", fillColor="black", autoDraw=True)
myline6 = visual.Rect(win, width=1, height=50, lineColor="black", fillColor="black", autoDraw=True)
myline7 = visual.Rect(win, width=1, height=50, lineColor="black", fillColor="black", autoDraw=True)
myline8 = visual.Rect(win, width=1, height=50, lineColor="black", fillColor="black", autoDraw=True)
myline9 = visual.Rect(win, width=1, height=100, lineColor="black", fillColor="black", autoDraw=True)
myline10 = visual.Rect(win, width=100, height=1, lineColor="black", fillColor="black", autoDraw=True)
myline11 = visual.Rect(win, width=100, height=1, lineColor="black", fillColor="black", autoDraw=True)
myline12 = visual.Rect(win, width=200, height=1, lineColor="black", fillColor="black", autoDraw=True)
myline13 = visual.Rect(win, width=202, height=1, lineColor="black", fillColor="black", autoDraw=True)
myline14 = visual.Rect(win, width=250, height=1, lineColor="black", fillColor="black", autoDraw=True)
myline15 = visual.Rect(win, width=250, height=1, lineColor="black", fillColor="black", autoDraw=True)
myline16 = visual.Rect(win, width=1, height=200, lineColor="black", fillColor="black", autoDraw=True)

#Draw lines
myline1.pos = (-301,51)
myline2.pos = (-201,101)
myline3.pos = (-151,75)
myline4.pos = (-175,50)
myline5.pos = (+175,50)
myline6.pos = (+151,25)
myline7.pos = (-99,-25)
myline8.pos = (+99,125)
myline9.pos = (+201,0)
myline10.pos = (-251,152)
myline11.pos = (+251,-50)
myline12.pos = (-200,-50)
myline13.pos = (+200,151)
myline14.pos = (-25,101)
myline15.pos = (25,0)
myline16.pos = (+301,51)

# Draw start and finish rects
mygreenrect2 = visual.Rect(win, width=100, height=200, lineColor="green", fillColor="green", autoDraw=True)
mygreenrect3 = visual.Rect(win, width=100, height=200, lineColor="green", fillColor="green", autoDraw=True)
mygreenrect2.pos = (-251,51)
mygreenrect3.pos = (+251,49)

#Draw checkered pattern
stim = visual.ImageStim(win, image=tex,pos=(0,50), size=100,)
stim2 = visual.ImageStim(win, image=tex,pos=(100,50), size=100)
stim3 = visual.ImageStim(win, image=tex,pos=(-100,50), size=100)
stim4 = visual.ImageStim(win, image=tex2,pos=(+150,100), size=100)
stim5 = visual.ImageStim(win, image=tex2,pos=(-150,0), size=100)

stim.autoDraw = True
stim2.autoDraw = True
stim3.autoDraw = True
stim4.autoDraw = True
stim5.autoDraw = True

# Draw main rectangle
myrect = visual.Rect(win, width=15, height=15, lineColor="black", fillColor="red", autoDraw = True)

# Responses
keys = key.KeyStateHandler()
win.winHandle.push_handlers(keys)

#Draw balls/enemies
img1 = visual.ImageStim(win, image="ball.png")
img2 = visual.ImageStim(win, image="ball.png")
img3 = visual.ImageStim(win, image="ball.png")
img4 = visual.ImageStim(win, image="ball.png")
img1.autoDraw = True
img2.autoDraw = True
img3.autoDraw = True
img4.autoDraw = True

#Draw  main rectangle
myrect.pos = (-250,100)

# Movement of the ball
positions = 150 * np.sin(np.linspace( 2 * np.pi,0, 150))
#Speed of the main character/square
inc = 10
#Speed of the ball
x = 3

while True:
    
    #Display Score
    score(visual,win,x)

    
    for pos in range(-140,140,+x):

        #Define gameover
        gameover(13,38,63,88,myrect,img1,img2,img3,img4,pos,win,core,visual,x)
        win.flip()
       
        #Define movement and collision logic
        movementandcollisionlogic(keys,key,myrect,pos,scr_size,inc,myline1,myline2,myline3,myline4,myline5,myline6,myline7,myline8,myline9,myline10)    
            
        #Define exit
        exit(keys,key,win,core)
    
        #Define success
        x = levelup(myrect,win,x,visual,core)        
        
    for pos in range(140,-140,-x):
        
        #Define gameover
        gameover(13,38,63,88,myrect,img1,img2,img3,img4,pos,win,core,visual,x)
        win.flip()
   
        #Define movement and collision logic
        movementandcollisionlogic(keys,key,myrect,pos,scr_size,inc,myline1,myline2,myline3,myline4,myline5,myline6,myline7,myline8,myline9,myline10)    
            
        #Define exit
        exit(keys,key,win,core)
        
        #Define success
        x = levelup(myrect,win,x,visual,core)               
        
#end game
end(core,win)
    
    
    
    

def levelup(myrect,win,x,visual,core):

    if  myrect.pos[0] in range(+198,+300) and myrect.pos[1] in range(50,150):
        myrect.pos = (-250,100)
        txt = visual.TextStim(win,text="KEEP GOING !!!",font='10',pos=(0.0, -50.0), rgb=None, color=(0.1, 0.1, 0.1), colorSpace='rgb')
        txt.draw()
        win.flip()
        core.wait(1)

        return x+1
        win.flip()
        
    
    else:
        return x
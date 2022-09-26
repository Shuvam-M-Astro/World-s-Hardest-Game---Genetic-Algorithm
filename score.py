def score(visual,win,x):

    scoreboard = visual.Rect(win, width=200, height=20, lineColor="white", fillColor="white", autoDraw=True)
    scoreboard.pos = (+220,200)
    txt2 = visual.TextStim(win, text="Level:{}".format(x-1),pos=(200.0, 200.0), rgb=None, color=(0.1, 0.1, 0.1), colorSpace='rgb')
    txt2.setAutoDraw(True)
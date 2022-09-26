def movementandcollisionlogic(keys,key,myrect,pos,scr_size,inc,myline1,myline2,myline3,myline4,myline5,myline6,myline7,myline8,myline9,myline10):



        if keys[key.LEFT] and myrect.pos[0] - myrect.width / 2 > scr_size[0] and myrect.pos[0] in range(-289,-200) and myrect.pos[1] in range(-50,150) or keys[key.LEFT] and myrect.pos[0] in range(-200,-100) and myrect.pos[1] in range(-50,50)  or keys[key.LEFT] and myrect.pos[0] in range(-139,+151) and myrect.pos[1] in range(0,100):
            myrect.pos -= (inc, 0)
        
        if keys[key.LEFT] and myrect.pos[0] in range(+112,+200) and myrect.pos[1] in range(50,150):
            myrect.pos -= (inc, 0)
        
        if keys[key.RIGHT] and myrect.pos[0] + myrect.width / 2 < scr_size[2] and myrect.pos[0] in range(-301,-214) and myrect.pos[1] in range(-50,150) or keys[key.RIGHT] and myrect.pos[0] in range(-214,-112) and myrect.pos[1] in range(-50,50)  or keys[key.RIGHT] and myrect.pos[0] in range(-151,+139) and myrect.pos[1] in range(0,100):
            myrect.pos += (inc, 0)
            
        if keys[key.RIGHT] and myrect.pos[0] in range(+100,+200) and myrect.pos[1] in range(50,150):
            myrect.pos += (inc, 0)
            
        if keys[key.UP] and myrect.pos[1] + myrect.height / 2 < scr_size[1] and abs(myrect.pos[1] - myline10.pos[1]) > 12 and myrect.pos[0] in range(-301,-201) or keys[key.UP] and myrect.pos[0] in range(-201,-101) and myrect.pos[1] in range(-50,38) or keys[key.UP] and myrect.pos[0] in range(-151,+151) and myrect.pos[1] in range(0,88):
            myrect.pos += (0, inc)
        
        if keys[key.UP] and myrect.pos[0] in range(+100,+200) and myrect.pos[1] in range(36,138):
            myrect.pos += (0, inc)
        
        if keys[key.DOWN] and myrect.pos[1] - myrect.height / 2 > scr_size[3] and myrect.pos[0] in range(-303,-201) and myrect.pos[1] in range(-38,150) or keys[key.DOWN] and myrect.pos[0] in range(-201,-101) and myrect.pos[1] in range(-38,50) or keys[key.DOWN] and myrect.pos[0] in range(-151,+151) and myrect.pos[1] in range(12,100):
            myrect.pos -= (0, inc)
            
        if keys[key.DOWN] and myrect.pos[0] in range(+100,+200) and myrect.pos[1] in range(62,150):
            myrect.pos -= (0, inc)
import subprocess
setThrowException(True)
import datetime

def print_time(msg):
    tt = datetime.datetime.now().strftime("%H:%M:%S.%f")
    print( "%s  %s" % (tt, msg) )

def myClick(pos):
    if not pos:
        return
    pos.hover()
    mouseDown(Button.LEFT)
    sleep(0.1)
    mouseUp()
    sleep(0.1)

Settings.MoveMouseDelay = 0.2

#setting
#pick all
#pick_mode = 1 
#pick only ball
#pick_mode = 2 
pick_mode = 1
store = 1

fishing_rod = '7'
is_shooting = 0
count = 0
count2 = 0
is_fishing = 0

while True:
        m1 = False
        if is_fishing > 0:
            m1 = exists(Pattern("1506221481654.png").similar(0.50),is_fishing)
        is_fishing = 0
        if m1:
            r1 = Region(m1.x - int(m1.w*0.18), m1.y + int(m1.h*2.6), int(m1.w*1.45), int(m1.h*0.5))
            img1 = capture(r1)
            sleep(0.1)
            img2 = capture(r1)
            result = subprocess.check_output('cd /d %s && cd ../../python && python darwin.py %s %s'%(getBundlePath(),img1,img2), shell=True)
            print(result)
            type(result)
            if pick_mode == 1:
                sleep(4)
                type("r")
            elif pick_mode == 2:
                sleep(3.5)
                if exists("1506187210848.png",0):
                    type("r")
            type(Key.SPACE)
            is_shooting = 0
            sleep(3)
            if exists("1506871959078.png",0):
                myClick(exists("1508600299846.png",0))
        #print_time("f2")
        if exists("1506065189732.png",0):
            type(Key.SPACE)
            sleep(1.60+0.1)
            type(Key.SPACE)
            is_shooting = 0
            count += 1
            is_fishing = 5
            continue
        #print_time("f3")
        if exists("1506065112873.png",0):
            if is_shooting == 1:
                if fishing_rod == '7':
                    fishing_rod = '8'
                else:
                    fishing_rod = '7'
                type(fishing_rod)
                sleep(1)
            is_shooting = 1
            if pick_mode == 1:
                type("r")
            elif pick_mode == 2:
                if exists("1506187210848.png",0):
                    type("r")
            type(Key.SPACE)
            t1 = datetime.datetime.now()
            sleep(5)
            if exists("1506819135171.png",0):
                type(Key.ESC)
            if exists("1506819529645.png",0):
                type(Key.ESC)
            if exists("1508342707927.png",0):
                type(Key.ESC)
        if exists("1508519043012.png",0):
            if exists("1506871959078.png",0):
                myClick(exists("1508600299846.png",0))
            if store == 1:
                myClick(exists("1509104285011.png",0))
                store = 2
            elif store == 2:
                myClick(exists("1509352787893.png",0))
                store = 1
            sleep(1)
            m2 = exists("1508519764906.png",0)
            if not m2:
                continue
            r2 = Location(m2.x, m2.y + 60)
            myClick(r2)
            sleep(1)
            try:
                if exists("1506937021194.png",0):
                    for x in findAll("1506937021194.png"):
                        myClick(x)
                        type(Key.ENTER)
                    if exists("1506937045640.png",35):
                        iten_count = 0
                        for x in findAll("1506937045640.png"):
                            myClick(x)
                            type(Key.ENTER)
                            count2 += 1
                            iten_count += 1
                        if iten_count > 1:
                            if exists("1506937045640.png",0):
                                for x in findAll("1506937045640.png"):
                                    myClick(x)
                                    type(Key.ENTER)
                                    count2 += 1
            except:
                continue
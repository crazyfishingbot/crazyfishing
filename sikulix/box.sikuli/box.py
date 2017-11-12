
def myClick(pos):
    pos.hover()
    mouseDown(Button.LEFT)
    sleep(0.1)
    mouseUp()
    sleep(1)

def myClick_r(pos):
    pos.hover()
    mouseDown(Button.RIGHT)
    sleep(0.1)
    mouseUp()
    sleep(1)

def making():
    sleep(1)
    type('w')
    sleep(1)
    type('w')
    sleep(1)
    type('r')
    sleep(1)
    myClick(exists("1509639548557.png",0))
    #myClick(Location(621, 259))
    product = Location(1723, 670)
    myClick_r(product)
    type(Key.ENTER)
    sleep(1)
    myClick_r(product)
    type(Key.ENTER)
    sleep(1)
    myClick(exists("1509609684238.png",0))
    #myClick(Location(971, 674))
    myClick(exists("1509609735318.png",0))
    myClick_r(Location(1534, 645))
    myClick(exists("1509609804249.png",0))
    type(Key.CTRL)
    sleep(1)
    myClick(Location(224, 132))
    myClick(Location(1498, 655))


while True:
    if exists("1506819135171-1.png",0):
            type(Key.ESC)
    if exists("1506819529645-1.png",0):
        type(Key.ESC)
    if exists("1506871959078.png",0):
        myClick(Location(1276, 340))
    if not Region(834,829,251,102).exists("1509639792211.png",0):
        making()
    sleep(10)
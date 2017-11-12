setThrowException(True)

Settings.MoveMouseDelay = 0.2

def myClick(pos):
    pos.hover()
    mouseDown(Button.LEFT)
    sleep(0.1)
    mouseUp()
    sleep(0.1)

def m_findAll(ptn):
    try:
        return findAll(ptn)
    except:
        return []

while True:
    #if exists("1506936502299.png",0):
        #Location(934, 333).click()
        #Location(934, 333).click()
    
    #if exists("1506936596443.png",0):
    if exists("1506937021194.png",0):
        for x in m_findAll("1506937021194.png"):
            myClick(x)
            type(Key.ENTER)
    if exists("1506937045640.png",0):
        for x in m_findAll("1506937045640.png"):
            myClick(x)
            type(Key.ENTER)
    #for x in findAll("1506937084212.png"):
        #click(x)
        #click(x)
        #type(Key.ENTER)
    if exists("1508863694582.png",0):
        type(Key.ENTER)
    if exists("1506871959078.png",0):
        myClick(exists("1508935444167.png",0))
    refresh = exists("1506937618981.png",0)
    if refresh:
        myClick(refresh)
        #type(Key.BACKSPACE)
        
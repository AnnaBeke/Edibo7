from graphics import *

def logo():
    win = GraphWin('Anna', 300, 300)
    win.setBackground('white')
    cir=Circle(Point(150,150),120)
    cir.setOutline('indian red')
    cir.setWidth(7)
    cir.setFill('salmon')
    line1=Line(Point(150,40), Point (70,225))
    line2=Line(Point(150,40), Point(230,225))
    line3=Line(Point(105,150),Point(195,150))
    line1.setOutline('white')
    line2.setOutline('white')
    line3.setOutline('white')
    line1.setWidth(10)
    line2.setWidth(10)
    line3.setWidth(10)
    cir2=Circle(Point(150,150),110)
    cir2.setOutline('white')
    cir2.setWidth(4)


    cir.draw(win)
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    cir2.draw(win)

    win.getMouse()
    win.close()

logo()
import turtle as t

'''
x = x position
y = y position
w = width
h = height
f = fill color
'''
def fill_rect(**rectoptions):
    print(rectoptions["x"])
    print(rectoptions["y"])
    print(rectoptions["w"])
    print(rectoptions["h"])
    print(rectoptions["f"])
    '''
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.fillcolor(f)
    t.begin_fill()
    for i in range(2):
        t.fd(w)
        t.rt(90)
        t.fd(h)
        t.rt(90)
    t.end_fill()
    '''
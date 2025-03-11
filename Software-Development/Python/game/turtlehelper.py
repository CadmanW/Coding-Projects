class TurtleHelper:

    @staticmethod
    def fill_rect(**rect):
        '''
        x = x position
        y = y position
        w = width
        h = height
        f = fill color
        s = stroke color
        t = turtle
        '''

        x = rect["x"]
        y = rect["y"]
        w = rect["w"]
        h = rect["h"]
        f = rect["f"]
        turtle = rect["t"]
        
        turtle.pu()
        turtle.goto(x, y)
        turtle.fillcolor(f)

        turtle.begin_fill()
        for _ in range(2):
            turtle.fd(w)
            turtle.seth(turtle.heading() + 90)
            turtle.fd(h)
            turtle.seth(turtle.heading() + 90)
        turtle.end_fill()
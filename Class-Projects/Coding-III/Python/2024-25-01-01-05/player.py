from turtlehelpers import TurtleHelpers

class Player():
    def __init__(self, **options):
        ''' 
        Options:
            t = turtle
            x = x position
            y = y position
            w = width
            h = height
            c = color
        '''
        self.turtle = options["t"]
        self.x = options["x"]
        self.y = options["y"]
        self.w = options["w"]
        self.h = options["h"]
        self.c = options["c"]

    def move(self):
        pass
    
    def draw(self):
        """
        1) draw the background rect
            * a rect should be drawn starting at point (x, y) to the point (w, h)
        2) draw the color rect
            * same as step 1) but...
                the starting point should be incremeneted by 6 to the points (w, h)
        3) draw the eyeballs
            3.1) draw the left eye
            * same as step 1) but ...
                the starting point should be incremented by 18 to the point (w, h)
            3.2) draw the right eye
                the starting point x sould be incremented by 
        4) draw the pupils
            4.1) draw the left pupil
            4.2) draw the right pupil
        """
        TurtleHelpers.fill_rect(self)

    def take_hit(self):
        pass
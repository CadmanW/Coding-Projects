from turtlehelper import TurtleHelper

PLAYER_BLACK = "#222222"
PLAYER_WHITE = "#F2F2F2"
PLAYER_BLUE = "#50B4F2"
PLAYER_RED = "#F24949"
PLAYER_ORANGE = "#F2B705"
PLAYER_YELLOW = "#F2E41D"

class Player():
    def __init__(self, **options):
        self.t = options["t"]
        self.x = options["x"]
        self.y = options["y"]
        self.w = options["w"]
        self.h = options["h"]
        self.c = options["c"]

    def _update(self):
        # Background
        TurtleHelper.fill_rect(x=self.x, y=self.y, w=self.w, h=self.h, f=PLAYER_BLACK, t=self.t)
        # Color Rectangle
        TurtleHelper.fill_rect(x=self.x+8, y=self.y+8, w=self.w-16, h=self.h-16, f=self.c, t=self.t)
        # Eyeball Rectangles
        TurtleHelper.fill_rect(x=self.x+24, y=self.y+24, w=self.w-96, h=self.h-96, f=PLAYER_WHITE, t=self.t)
        TurtleHelper.fill_rect(x=self.x+72, y=self.y+24, w=self.w-96, h=self.h-96, f=PLAYER_WHITE, t=self.t)
        # Pupil Rectangles
        TurtleHelper.fill_rect(x=self.x+32, y=self.y+32, w=self.w-112, h=self.h-112, f=PLAYER_BLACK, t=self.t)
        TurtleHelper.fill_rect(x=self.x+80, y=self.y+32, w=self.w-112, h=self.h-112, f=PLAYER_BLACK, t=self.t)

    def move(self, key):
        self._update()
        # TO-DO start here
        print(f"player should moce {key}")
    
    def draw(self):
        self._update()

    def take_hit(self):
        pass
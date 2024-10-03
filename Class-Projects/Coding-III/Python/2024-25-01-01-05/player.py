from turtlehelper import TurtleHelper
from basetile import BaseTile

PLAYER_BLACK = "#222222"
PLAYER_WHITE = "#F2F2F2"
PLAYER_BLUE = "#50B4F2"
PLAYER_RED = "#F24949"
PLAYER_ORANGE = "#F2B705"
PLAYER_YELLOW = "#F2E41D"

class Player(BaseTile):
    def __init__(self, **options):
        self.t = options["t"]
        self.x = options["x"]
        self.y = options["y"]
        self.width = options["w"]
        self.height = options["h"]
        self.f = options["f"]
        self.position = (self.x, self.y)

    def _update(self):
        # Resetting the tile we're moving from
        TurtleHelper.fill_rect(x=self.position[0], y=self.position[1], w=self.width, h=self.height, f="black", t=self.t)
        # Background
        TurtleHelper.fill_rect(x=self.x, y=self.y, w=self.width, h=self.height, f=PLAYER_BLACK, t=self.t)
        # Color Rectangle
        TurtleHelper.fill_rect(x=self.x+8, y=self.y+8, w=self.width-16, h=self.height-16, f=self.f, t=self.t)
        # Eyeball Rectangles
        TurtleHelper.fill_rect(x=self.x+24, y=self.y+24, w=self.width-96, h=self.height-96, f=PLAYER_WHITE, t=self.t)
        TurtleHelper.fill_rect(x=self.x+72, y=self.y+24, w=self.width-96, h=self.height-96, f=PLAYER_WHITE, t=self.t)
        # Pupil Rectangles
        TurtleHelper.fill_rect(x=self.x+32, y=self.y+32, w=self.width-112, h=self.height-112, f=PLAYER_BLACK, t=self.t)
        TurtleHelper.fill_rect(x=self.x+80, y=self.y+32, w=self.width-112, h=self.height-112, f=PLAYER_BLACK, t=self.t)

        self.position = (self.x, self.y)



    def move(self, key, map_width, map_height):
        match key:
            case "Up":
                if self.y >= self.width:
                    self.y -= self.width
                    self._update()

            case "Down":
                if self.y < map_height - self.width:
                    self.y +- self.width
                    self._update()

            case "Left":
                if self.x >= self.width:
                    self.x -= self.width
                    self._update()

            case "Right":
                if self.x < map_width - self.width:
                    self.x += self.width
                    self._update()
        


    def draw(self):
        self._update()

    def take_hit(self):
        pass
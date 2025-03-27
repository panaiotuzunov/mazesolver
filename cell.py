from graphics import Line, Point, Window


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = False
        self.has_top_wall = False
        self.has_bottom_wall = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            Line(Point(x1, y1), Point(x1, y2)).draw(self._win.canvas, "black")
        if self.has_right_wall:
            pass
        if self.has_top_wall:
            pass
        if self.has_bottom_wall:
            pass
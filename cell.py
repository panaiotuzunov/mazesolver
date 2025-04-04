from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.center = None
        self.visited = False

    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            Line(Point(x1, y1), Point(x1, y2)).draw(self._win.canvas, "black")
        else:
            Line(Point(x1, y1), Point(x1, y2)).draw(self._win.canvas, "white")
        if self.has_right_wall:
            Line(Point(x2, y1), Point(x2, y2)).draw(self._win.canvas, "black")
        else:
            Line(Point(x2, y1), Point(x2, y2)).draw(self._win.canvas, "white")
        if self.has_top_wall:
            Line(Point(x1, y1), Point(x2, y1)).draw(self._win.canvas, "black")
        else:
            Line(Point(x1, y1), Point(x2, y1)).draw(self._win.canvas, "white")
        if self.has_bottom_wall:
            Line(Point(x1, y2), Point(x2, y2)).draw(self._win.canvas, "black")
        else:
            Line(Point(x1, y2), Point(x2, y2)).draw(self._win.canvas, "white")
        self.center = Point((x1 + x2) / 2, (y1 + y2) / 2)


    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        line = Line(self.center, to_cell.center)
        line.draw(self._win.canvas, fill_color)


    

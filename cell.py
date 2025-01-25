from shapes import Point, Line

class Cell:
    def __init__(self, win=None, x1=None, x2=None, y1=None, y2=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self, fill_color):
        if self._win is None:
            return
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, fill_color)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, fill_color)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, fill_color)
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, fill_color)

    def draw_move(self, to_cell, undo=False):
        color = 'grey' if undo else 'red'
        line = Line(self.get_center(), to_cell.get_center())
        self._win.draw_line(line, color)
            
    def get_center(self):
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        return Point(center_x, center_y)
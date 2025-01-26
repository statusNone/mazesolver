from shapes import Point, Line

class Wall:
    def __init__(self, start, end, win=None):
        self._start = start
        self._end = end
        self._win = win
        self._is_present = True

    def draw(self):
        if self._win is None:
            return
        color = 'black' if self._is_present else self._win._bg_color
        self._win.draw_line(Line(self._start, self._end), color)

    def remove(self):
        self._is_present = False
        self.draw()
        

class Cell:
    def __init__(self, win=None):
        self._right_wall = None
        self._left_wall = None
        self._top_wall = None
        self._bottom_wall = None
        self._win = win
        self.visited = False

    def update_walls(self, x1, x2, y1, y2):
        self._left_wall = Wall(Point(x1, y1), Point(x1, y2), self._win)
        self._right_wall = Wall(Point(x2, y1), Point(x2, y2), self._win)
        self._top_wall = Wall(Point(x1, y1), Point(x2, y1), self._win)
        self._bottom_wall = Wall(Point(x1, y2), Point(x2, y2), self._win)

    def draw(self):
        if self._win is None:
            return
        self._right_wall.draw()
        self._left_wall.draw()
        self._top_wall.draw()
        self._bottom_wall.draw()

    def draw_move(self, to_cell, undo=False):
        color = 'grey' if undo else 'red'
        line = Line(self.get_center(), to_cell.get_center())
        self._win.draw_line(line, color)
            
    def get_center(self):
        # Can use any wall's points, let's use left wall
        start = self._left_wall._start
        # Could use either right wall's start or left wall's end for the x2
        end = self._right_wall._start
        center_x = (start.x + end.x) / 2
        center_y = (start.y + end.y) / 2
        return Point(center_x, center_y)
    
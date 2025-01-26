from cell import Cell
import time, random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = {}
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = random.seed(seed) if seed else None


        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_rows):  # i for rows
            for j in range(self._num_cols):  # j for columns
                self._cells[(i, j)] = Cell(self._win)
        for (i, j) in self._cells.keys():
            self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[(i, j)].update_walls(x1, x2, y1, y2)
        if self._win is not None:
            self._cells[(i, j)].draw()
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[(0, 0)]._left_wall.remove()
        self._cells[(self._num_rows - 1, self._num_cols - 1)]._right_wall.remove()

    def _break_walls_r(self, i, j):
        self._cells[(i, j)].visited = True
        directions = [
            (-1, 0, '_top_wall', '_bottom_wall'),  # Up
            (1, 0, '_bottom_wall', '_top_wall'),  # Down
            (0, -1, '_left_wall', '_right_wall'),  # Left
            (0, 1, '_right_wall', '_left_wall')   # Right
        ]

        while True:
            possible_moves = []
            for di, dj, current_wall, neighbor_wall in directions:
                new_i = i + di
                new_j = j + dj
                
                if (0 <= new_i < self._num_rows and 
                    0 <= new_j < self._num_cols and 
                    not self._cells[(new_i, new_j)].visited):
                    possible_moves.append((new_i, new_j, current_wall, neighbor_wall))

            if not possible_moves:
                return  # No more moves possible from this cell

            # Pick random direction and break walls
            new_i, new_j, current_wall, neighbor_wall = random.choice(possible_moves)
            getattr(self._cells[(i, j)], current_wall).remove()
            getattr(self._cells[(new_i, new_j)], neighbor_wall).remove()

            # Recursively visit new cell
            self._break_walls_r(new_i, new_j)
            # Don't return here - continue the while loop to check other possible moves
    
    def _reset_cells_visited(self):
        for (i, j) in self._cells.keys():
            self._cells[(i, j)].visited = False


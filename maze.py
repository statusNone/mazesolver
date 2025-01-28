from cell import Cell
import time, random
from shapes import Line, Point

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
        self._solve_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_rows):  # i for rows
            for j in range(self._num_cols):  # j for columns
                self._cells[(i, j)] = Cell(i, j, self._win)
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

    def _get_possible_moves(self, i, j):
        """Get unvisited neighboring cells."""
        offsets = {
            'up': (i - 1, j),
            'down': (i + 1, j),
            'left': (i, j - 1),
            'right': (i, j + 1)
        }
        return {
            direction: self._cells[neighbor]
            for direction, neighbor in offsets.items()
            if neighbor in self._cells and not self._cells[neighbor].visited
        }

    def _break_walls_r(self, i, j):
        """Recursively generate a maze by breaking walls between cells."""
        self._cells[(i, j)].visited = True

        while True:
            possible_moves = self._get_possible_moves(i, j)
            if not possible_moves:
                return  # No more moves possible from this cell

            # Pick a random direction and neighbor
            direction, neighbor = random.choice(list(possible_moves.items()))

            # Break walls between current cell and the chosen neighbor
            walls = {
                'up': ('_top_wall', '_bottom_wall'),
                'down': ('_bottom_wall', '_top_wall'),
                'left': ('_left_wall', '_right_wall'),
                'right': ('_right_wall', '_left_wall'),
            }
            getattr(self._cells[(i, j)], walls[direction][0]).remove()
            getattr(neighbor, walls[direction][1]).remove()

            # Recursively visit the chosen neighbor
            self._break_walls_r(*neighbor.location)

    def _reset_cells_visited(self):
        """Reset the visited status of all cells."""
        for cell in self._cells.values():
            cell.visited = False

    def _solve_r(self, i, j):
        """Recursively solve the maze."""
        self._animate()
        self._cells[(i, j)].visited = True

        # Base case: Reached the end of the maze
        if (i, j) == (self._num_rows - 1, self._num_cols - 1):
            return True

        directions = [
            (-1, 0, '_top_wall', '_bottom_wall'),  # Up
            (1, 0, '_bottom_wall', '_top_wall'),  # Down
            (0, -1, '_left_wall', '_right_wall'),  # Left
            (0, 1, '_right_wall', '_left_wall'),  # Right
        ]

        for di, dj, current_wall, neighbor_wall in directions:
            new_i, new_j = i + di, j + dj
            if (
                0 <= new_i < self._num_rows
                and 0 <= new_j < self._num_cols
                and not getattr(self._cells[(i, j)], current_wall)._is_present
                and not self._cells[(new_i, new_j)].visited
            ):
                self._cells[(i, j)].draw_move(self._cells[(new_i, new_j)])
                if self._solve_r(new_i, new_j):
                    return True
                self._cells[(i, j)].draw_move(self._cells[(new_i, new_j)], undo=True)

        return False

    def solve(self):
        """Solve the maze starting from the top-left corner."""
        self._reset_cells_visited()
        return self._solve_r(0, 0)

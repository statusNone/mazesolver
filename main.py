from window import Window
from cell import Cell

def main():
    # Create a window
    win = Window(800, 600)
    
    # Create cells of different sizes/positions
    cell1 = Cell(win, 50, 100, 50, 100)  # top-left cell
    cell1.draw("red")
    
    # Create adjacent cell with shared wall removed
    cell2 = Cell(win, 100, 150, 50, 100)  # cell to the right
    cell2.has_left_wall = False  # remove shared wall
    cell2.draw("blue")

    win.wait_for_close()

if __name__ == "__main__":
    main()
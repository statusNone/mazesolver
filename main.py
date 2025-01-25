from window import Window
from maze import Maze

def main():
    # Create a window
    win = Window(800, 800)
    num_cols = 12
    num_rows = 10
    # Create Maze
    m1 = Maze(100, 100, num_rows, num_cols, 10, 10, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
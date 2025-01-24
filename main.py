from window import Window
from shapes import Point, Line

def main():
    win = Window(800, 600)
    
    # First, create some points
    point1 = Point(100, 100)
    point2 = Point(700, 500)
    
    # Then create a line using those points
    my_line = Line(point1, point2)
    
    # Now draw the line
    win.draw_line(my_line, 'black')
    
    win.wait_for_close()
    

if __name__ == "__main__":
    main()
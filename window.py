from tkinter import Tk, BOTH, Canvas
from shapes import Line

class Window():
    def __init__(self, height, width, title="Maze Solver"):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry(f"{self.width}x{self.height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self._bg_color = self.__root.cget('bg')
        
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color='black'):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
            
    def close(self):
        self.is_running = False

from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, pointA: Point, pointB: Point):
        self.pointA = pointA
        self.pointB = pointB

    def draw(self, canvas: Canvas, fillColor: str):
        canvas.create_line(self.pointA.x, self.pointA.y, self.pointB.x, self.pointB.y, fill=fillColor, width=2)
        
class Cell:
    def __init__(self):
        pass

class Window:
    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title = "Maze Runna"
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fillColor: str):
        line.draw(self.canvas, fillColor)


def main():
    win = Window(640, 600)

    win.draw_line(Line(Point(10, 60), Point(300, 300)), "black")

    win.wait_for_close()

    
    
if __name__ == "__main__":
    main()